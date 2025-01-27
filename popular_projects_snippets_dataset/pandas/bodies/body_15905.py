# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["A", "B", "C"])

for levels in ["A", "B"], [0, 1]:
    # With MultiIndex
    s = df.set_index(["A", "B"])["C"]

    result = s.reset_index(level=levels[0])
    tm.assert_frame_equal(result, df.set_index("B"))

    result = s.reset_index(level=levels[:1])
    tm.assert_frame_equal(result, df.set_index("B"))

    result = s.reset_index(level=levels)
    tm.assert_frame_equal(result, df)

    result = df.set_index(["A", "B"]).reset_index(level=levels, drop=True)
    tm.assert_frame_equal(result, df[["C"]])

    with pytest.raises(KeyError, match="Level E "):
        s.reset_index(level=["A", "E"])

    # With single-level Index
    s = df.set_index("A")["B"]

    result = s.reset_index(level=levels[0])
    tm.assert_frame_equal(result, df[["A", "B"]])

    result = s.reset_index(level=levels[:1])
    tm.assert_frame_equal(result, df[["A", "B"]])

    result = s.reset_index(level=levels[0], drop=True)
    tm.assert_series_equal(result, df["B"])

    with pytest.raises(IndexError, match="Too many levels"):
        s.reset_index(level=[0, 1, 2])

        # Check that .reset_index([],drop=True) doesn't fail
result = Series(range(4)).reset_index([], drop=True)
expected = Series(range(4))
tm.assert_series_equal(result, expected)
