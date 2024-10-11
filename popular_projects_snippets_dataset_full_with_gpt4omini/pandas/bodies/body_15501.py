# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_round.py
datetime_series.index.name = "index_name"
result = datetime_series.round(2)
expected = Series(
    np.round(datetime_series.values, 2), index=datetime_series.index, name="ts"
)
tm.assert_series_equal(result, expected)
assert result.name == datetime_series.name
