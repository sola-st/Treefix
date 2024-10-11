# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
df = DataFrame(
    {"A": [1, 2, 3, 4], "B": [2, np.nan, 4, 4]}, index=["a", "b", "c", "d"]
)
s = Series([1, 3, 11, 4], index=["a", "b", "c", "d"])
expected = DataFrame(False, index=df.index, columns=df.columns)
expected.loc["a", "A"] = True
expected.loc["d"] = True
result = df.isin(s)
tm.assert_frame_equal(result, expected)
