# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

with ensure_clean_store(setup_path) as store:

    with catch_warnings(record=True):

        # select with columns=
        df = tm.makeTimeDataFrame()
        _maybe_remove(store, "df")
        store.append("df", df)
        result = store.select("df", columns=["A", "B"])
        expected = df.reindex(columns=["A", "B"])
        tm.assert_frame_equal(expected, result)

        # equivalently
        result = store.select("df", [("columns=['A', 'B']")])
        expected = df.reindex(columns=["A", "B"])
        tm.assert_frame_equal(expected, result)

        # with a data column
        _maybe_remove(store, "df")
        store.append("df", df, data_columns=["A"])
        result = store.select("df", ["A > 0"], columns=["A", "B"])
        expected = df[df.A > 0].reindex(columns=["A", "B"])
        tm.assert_frame_equal(expected, result)

        # all a data columns
        _maybe_remove(store, "df")
        store.append("df", df, data_columns=True)
        result = store.select("df", ["A > 0"], columns=["A", "B"])
        expected = df[df.A > 0].reindex(columns=["A", "B"])
        tm.assert_frame_equal(expected, result)

        # with a data column, but different columns
        _maybe_remove(store, "df")
        store.append("df", df, data_columns=["A"])
        result = store.select("df", ["A > 0"], columns=["C", "D"])
        expected = df[df.A > 0].reindex(columns=["C", "D"])
        tm.assert_frame_equal(expected, result)
