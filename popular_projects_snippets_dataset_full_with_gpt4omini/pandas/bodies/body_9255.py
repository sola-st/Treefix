# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/31503
ser = Series(range(3))
idx = Categorical([True, False, None])
if index:
    idx = CategoricalIndex(idx)

result = ser[idx]
expected = ser[idx.fillna(False)]

tm.assert_series_equal(result, expected)
