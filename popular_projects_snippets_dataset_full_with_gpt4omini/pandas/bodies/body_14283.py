# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:

    df = DataFrame(
        {"A1": np.random.randn(20), "A2": np.random.randn(20)},
        index=np.arange(20),
    )
    df.loc[0:15, :] = np.nan

    # nan some entire rows (dropna=True)
    _maybe_remove(store, "df")
    store.append("df", df[:10], dropna=True)
    store.append("df", df[10:], dropna=True)
    tm.assert_frame_equal(store["df"], df[-4:])

    # nan some entire rows (dropna=False)
    _maybe_remove(store, "df2")
    store.append("df2", df[:10], dropna=False)
    store.append("df2", df[10:], dropna=False)
    tm.assert_frame_equal(store["df2"], df)

    # tests the option io.hdf.dropna_table
    with pd.option_context("io.hdf.dropna_table", False):
        _maybe_remove(store, "df3")
        store.append("df3", df[:10])
        store.append("df3", df[10:])
        tm.assert_frame_equal(store["df3"], df)

    with pd.option_context("io.hdf.dropna_table", True):
        _maybe_remove(store, "df4")
        store.append("df4", df[:10])
        store.append("df4", df[10:])
        tm.assert_frame_equal(store["df4"], df[-4:])

        # nan some entire rows (string are still written!)
        df = DataFrame(
            {
                "A1": np.random.randn(20),
                "A2": np.random.randn(20),
                "B": "foo",
                "C": "bar",
            },
            index=np.arange(20),
        )

        df.loc[0:15, :] = np.nan

        _maybe_remove(store, "df")
        store.append("df", df[:10], dropna=True)
        store.append("df", df[10:], dropna=True)
        tm.assert_frame_equal(store["df"], df)

        _maybe_remove(store, "df2")
        store.append("df2", df[:10], dropna=False)
        store.append("df2", df[10:], dropna=False)
        tm.assert_frame_equal(store["df2"], df)

        # nan some entire rows (but since we have dates they are still
        # written!)
        df = DataFrame(
            {
                "A1": np.random.randn(20),
                "A2": np.random.randn(20),
                "B": "foo",
                "C": "bar",
                "D": Timestamp("20010101"),
                "E": datetime.datetime(2001, 1, 2, 0, 0),
            },
            index=np.arange(20),
        )

        df.loc[0:15, :] = np.nan

        _maybe_remove(store, "df")
        store.append("df", df[:10], dropna=True)
        store.append("df", df[10:], dropna=True)
        tm.assert_frame_equal(store["df"], df)

        _maybe_remove(store, "df2")
        store.append("df2", df[:10], dropna=False)
        store.append("df2", df[10:], dropna=False)
        tm.assert_frame_equal(store["df2"], df)
