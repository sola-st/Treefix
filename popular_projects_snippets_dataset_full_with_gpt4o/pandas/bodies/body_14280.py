# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:

    # this is allowed by almost always don't want to do it
    # tables.NaturalNameWarning):
    with catch_warnings(record=True):

        df = tm.makeTimeDataFrame()
        _maybe_remove(store, "df1")
        store.append("df1", df[:10])
        store.append("df1", df[10:])
        tm.assert_frame_equal(store["df1"], df)

        _maybe_remove(store, "df2")
        store.put("df2", df[:10], format="table")
        store.append("df2", df[10:])
        tm.assert_frame_equal(store["df2"], df)

        _maybe_remove(store, "df3")
        store.append("/df3", df[:10])
        store.append("/df3", df[10:])
        tm.assert_frame_equal(store["df3"], df)

        # this is allowed by almost always don't want to do it
        # tables.NaturalNameWarning
        _maybe_remove(store, "/df3 foo")
        store.append("/df3 foo", df[:10])
        store.append("/df3 foo", df[10:])
        tm.assert_frame_equal(store["df3 foo"], df)

        # dtype issues - mizxed type in a single object column
        df = DataFrame(data=[[1, 2], [0, 1], [1, 2], [0, 0]])
        df["mixed_column"] = "testing"
        df.loc[2, "mixed_column"] = np.nan
        _maybe_remove(store, "df")
        store.append("df", df)
        tm.assert_frame_equal(store["df"], df)

        # uints - test storage of uints
        uint_data = DataFrame(
            {
                "u08": Series(
                    np.random.randint(0, high=255, size=5), dtype=np.uint8
                ),
                "u16": Series(
                    np.random.randint(0, high=65535, size=5), dtype=np.uint16
                ),
                "u32": Series(
                    np.random.randint(0, high=2**30, size=5), dtype=np.uint32
                ),
                "u64": Series(
                    [2**58, 2**59, 2**60, 2**61, 2**62],
                    dtype=np.uint64,
                ),
            },
            index=np.arange(5),
        )
        _maybe_remove(store, "uints")
        store.append("uints", uint_data)
        tm.assert_frame_equal(store["uints"], uint_data)

        # uints - test storage of uints in indexable columns
        _maybe_remove(store, "uints")
        # 64-bit indices not yet supported
        store.append("uints", uint_data, data_columns=["u08", "u16", "u32"])
        tm.assert_frame_equal(store["uints"], uint_data)
