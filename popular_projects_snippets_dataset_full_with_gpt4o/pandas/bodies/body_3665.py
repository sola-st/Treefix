# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# https://github.com/pandas-dev/pandas/issues/12392
df = DataFrame({"a": [1, 2], "b": [1, 2]}, index=["X", "Y"])
result = df.rename(index=str.lower, columns=str.upper)
expected = DataFrame({"A": [1, 2], "B": [1, 2]}, index=["x", "y"])
tm.assert_frame_equal(result, expected)
