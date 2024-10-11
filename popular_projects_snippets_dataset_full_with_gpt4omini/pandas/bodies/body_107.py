# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH20495
s = Series(vals + [np.nan])
result = s.map(mapping)

tm.assert_series_equal(result, Series(exp))
