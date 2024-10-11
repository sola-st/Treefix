# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#20049
# For historical reference see GH#14164, GH#13077.
# PeriodIndex subtraction originally performed set difference,
# then changed to raise TypeError before being implemented in GH#20049
rng = period_range("1/1/2000", freq="D", periods=5)
other = period_range("1/6/2000", freq="D", periods=5)

off = rng.freq
expected = pd.Index([-5 * off] * 5)
result = rng - other
tm.assert_index_equal(result, expected)

rng -= other
tm.assert_index_equal(rng, expected)
