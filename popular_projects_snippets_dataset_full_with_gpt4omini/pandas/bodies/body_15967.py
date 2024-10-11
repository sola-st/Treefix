# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
# see GH#9443

# sanity check
ser = Series(["a", "b", "a"], dtype="category")
exp = Series([2, 1], index=CategoricalIndex(["a", "b"]))

res = ser.value_counts(dropna=True)
tm.assert_series_equal(res, exp)

res = ser.value_counts(dropna=True)
tm.assert_series_equal(res, exp)

# same Series via two different constructions --> same behaviour
series = [
    Series(["a", "b", None, "a", None, None], dtype="category"),
    Series(
        Categorical(["a", "b", None, "a", None, None], categories=["a", "b"])
    ),
]

for ser in series:
    # None is a NaN value, so we exclude its count here
    exp = Series([2, 1], index=CategoricalIndex(["a", "b"]))
    res = ser.value_counts(dropna=True)
    tm.assert_series_equal(res, exp)

    # we don't exclude the count of None and sort by counts
    exp = Series([3, 2, 1], index=CategoricalIndex([np.nan, "a", "b"]))
    res = ser.value_counts(dropna=False)
    tm.assert_series_equal(res, exp)

    # When we aren't sorting by counts, and np.nan isn't a
    # category, it should be last.
    exp = Series([2, 1, 3], index=CategoricalIndex(["a", "b", np.nan]))
    res = ser.value_counts(dropna=False, sort=False)
    tm.assert_series_equal(res, exp)
