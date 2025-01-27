# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 46471
df = DataFrame({"x": [0, 1, np.nan]})

result = df.eval("x.fillna(-1)")
expected = df.x.fillna(-1)
# column name becomes None if using numexpr
# only check names when the engine is not numexpr
tm.assert_series_equal(result, expected, check_names=not USE_NUMEXPR)

result = df.eval("x.shift(1, fill_value=-1)")
expected = df.x.shift(1, fill_value=-1)
tm.assert_series_equal(result, expected, check_names=not USE_NUMEXPR)
