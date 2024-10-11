# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# Group the given series by a series with categorical data type such that group A
# takes indices 0 and 3 and group B indices 1 and 2, obtaining the values mapped in
# the given data.
groupby = series.groupby(Series(list("ABBA"), dtype="category"))
result = groupby.aggregate(list)
expected = Series(data, index=CategoricalIndex(data.keys()))
tm.assert_series_equal(result, expected)
