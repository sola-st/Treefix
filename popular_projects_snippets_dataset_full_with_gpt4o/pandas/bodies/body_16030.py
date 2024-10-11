# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
# https://github.com/pandas-dev/pandas/issues/27183
s = Series([None, None], dtype=object)
result = s.describe()
expected = Series(
    [0, 0, np.nan, np.nan],
    dtype=object,
    index=["count", "unique", "top", "freq"],
)
tm.assert_series_equal(result, expected)

result = s[:0].describe()
tm.assert_series_equal(result, expected)
# ensure NaN, not None
assert np.isnan(result.iloc[2])
assert np.isnan(result.iloc[3])
