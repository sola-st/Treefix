# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
s = Series(case, name="XXX")
res = s.quantile(0.5)
assert res == case[1]

res = s.quantile([0.5])
exp = Series([case[1]], index=[0.5], name="XXX")
tm.assert_series_equal(res, exp)
