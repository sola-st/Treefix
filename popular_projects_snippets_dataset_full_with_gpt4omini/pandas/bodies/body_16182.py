# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# float + int
int_ts = datetime_series.astype(int)[:-5]
added = datetime_series + int_ts
expected = Series(
    datetime_series.values[:-5] + int_ts.values,
    index=datetime_series.index[:-5],
    name="ts",
)
tm.assert_series_equal(added[:-5], expected)
