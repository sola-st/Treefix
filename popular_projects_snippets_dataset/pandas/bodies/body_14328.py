# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
with tm.ensure_clean(setup_path) as path:
    try:
        with HDFStore(path) as tbl:
            raise ValueError("blah")
    except ValueError:
        pass
with tm.ensure_clean(setup_path) as path:
    with HDFStore(path) as tbl:
        tbl["a"] = tm.makeDataFrame()
        assert len(tbl) == 1
        assert type(tbl["a"]) == DataFrame
