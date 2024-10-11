# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
index = Index(np.arange(10))
values = Series(np.ones(10), index, dtype=dtype)
labels = Series(
    [np.nan, "foo", "bar", "bar", np.nan, np.nan, "bar", "bar", np.nan, "foo"],
    index=index,
)

# this SHOULD be an int
grouped = values.groupby(labels)
agged = grouped.agg(len)
expected = Series([4, 2], index=["bar", "foo"])

tm.assert_series_equal(agged, expected, check_dtype=False)

# assert issubclass(agged.dtype.type, np.integer)

# explicitly return a float from my function
def f(x):
    exit(float(len(x)))

agged = grouped.agg(f)
expected = Series([4.0, 2.0], index=["bar", "foo"])

tm.assert_series_equal(agged, expected)
