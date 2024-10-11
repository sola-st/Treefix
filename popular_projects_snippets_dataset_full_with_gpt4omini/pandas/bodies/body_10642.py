# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#43701
data = Series(np.arange(20).reshape(10, 2).dot([1, 2j]))
result = data.groupby(data.index % 2).agg(func)
expected = Series(output)
tm.assert_series_equal(result, expected)
