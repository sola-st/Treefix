# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# Check that divmod uses pandas convention for division by zero,
#  which does not match numpy.
# pandas convention has
#  1/0 == np.inf
#  -1/0 == -np.inf
#  1/-0.0 == -np.inf
#  -1/-0.0 == np.inf
tser = tm.makeTimeSeries().rename("ts")
other = tser * 0

result = divmod(tser, other)
exp1 = Series([np.inf] * len(tser), index=tser.index, name="ts")
exp2 = Series([np.nan] * len(tser), index=tser.index, name="ts")
tm.assert_series_equal(result[0], exp1)
tm.assert_series_equal(result[1], exp2)
