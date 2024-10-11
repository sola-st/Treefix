# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with catch_warnings(record=True):

    def do_copy(f, new_f=None, keys=None, propindexes=True, **kwargs):
        if new_f is None:
            fd, new_f = tempfile.mkstemp()

        try:
            store = HDFStore(f, "r")
            tstore = store.copy(new_f, keys=keys, propindexes=propindexes, **kwargs)

            # check keys
            if keys is None:
                keys = store.keys()
            assert set(keys) == set(tstore.keys())

            # check indices & nrows
            for k in tstore.keys():
                if tstore.get_storer(k).is_table:
                    new_t = tstore.get_storer(k)
                    orig_t = store.get_storer(k)

                    assert orig_t.nrows == new_t.nrows

                    # check propindixes
                    if propindexes:
                        for a in orig_t.axes:
                            if a.is_indexed:
                                assert new_t[a.name].is_indexed

        finally:
            safe_close(store)
            safe_close(tstore)
            try:
                os.close(fd)
            except (OSError, ValueError):
                pass
            os.remove(new_f)

        # new table
    df = tm.makeDataFrame()

    with tm.ensure_clean() as path:
        with HDFStore(path) as st:
            st.append("df", df, data_columns=["A"])
        do_copy(f=path)
        do_copy(f=path, propindexes=False)
