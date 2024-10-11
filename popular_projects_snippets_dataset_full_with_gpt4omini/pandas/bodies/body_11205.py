# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH#47348
df = DataFrame({None: [1, 1, 2, 2], "b": [1, 1, 2, 3], "c": [4, 5, 6, 7]})
result = df.groupby(by=[None]).sum()
expected = DataFrame({"b": [2, 5], "c": [9, 13]}, index=Index([1, 2], name=None))
tm.assert_frame_equal(result, expected)
