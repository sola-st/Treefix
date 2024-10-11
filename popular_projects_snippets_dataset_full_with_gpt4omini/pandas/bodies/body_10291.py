# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
# https://github.com/pandas-dev/pandas/issues/23050
# Assert no 'Value Error : Length of passed values is 2, index implies 0'
df = DataFrame({"A": [None, None]})  # all-null groups
result = df.groupby("A").size()
expected = Series(dtype="int64", index=Index([], name="A"))
tm.assert_series_equal(result, expected)
