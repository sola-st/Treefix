# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
# https://github.com/pandas-dev/pandas/issues/11699
df = DataFrame(columns=["A", "B"])
out = Series(dtype="int64", index=Index([], name="A"))
tm.assert_series_equal(df.groupby("A").size(), out)
