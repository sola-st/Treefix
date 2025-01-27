# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

with tm.ensure_clean("__tmp_to_csv_from_csv2__") as path:

    # duplicate index
    df = DataFrame(
        np.random.randn(3, 3), index=["a", "a", "b"], columns=["x", "y", "z"]
    )
    df.to_csv(path)
    result = self.read_csv(path)
    tm.assert_frame_equal(result, df)

    midx = MultiIndex.from_tuples([("A", 1, 2), ("A", 1, 2), ("B", 1, 2)])
    df = DataFrame(np.random.randn(3, 3), index=midx, columns=["x", "y", "z"])

    df.to_csv(path)
    result = self.read_csv(path, index_col=[0, 1, 2], parse_dates=False)
    tm.assert_frame_equal(result, df, check_names=False)

    # column aliases
    col_aliases = Index(["AA", "X", "Y", "Z"])
    float_frame.to_csv(path, header=col_aliases)

    rs = self.read_csv(path)
    xp = float_frame.copy()
    xp.columns = col_aliases
    tm.assert_frame_equal(xp, rs)

    msg = "Writing 4 cols but got 2 aliases"
    with pytest.raises(ValueError, match=msg):
        float_frame.to_csv(path, header=["AA", "X"])
