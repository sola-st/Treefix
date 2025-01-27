# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series(np.nan, index=np.sort(np.random.rand(30)))
s[::3] = np.random.randn(10)

vals = s.index.values.astype(float)

result = s.interpolate(method="index")

expected = s.copy()
bad = isna(expected.values)
good = ~bad
expected = Series(
    np.interp(vals[bad], vals[good], s.values[good]), index=s.index[bad]
)

tm.assert_series_equal(result[bad], expected)

# 'values' is synonymous with 'index' for the method kwarg
other_result = s.interpolate(method="values")

tm.assert_series_equal(other_result, result)
tm.assert_series_equal(other_result[bad], expected)
