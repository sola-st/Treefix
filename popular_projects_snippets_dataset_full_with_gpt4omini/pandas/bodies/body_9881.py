# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# Tests that rolling window's quantile behavior is analogous to
# Series' quantile for each interpolation option
s = Series(data)

q1 = s.quantile(quantile, interpolation)
q2 = s.expanding(min_periods=1).quantile(quantile, interpolation).iloc[-1]

if np.isnan(q1):
    assert np.isnan(q2)
else:
    assert q1 == q2
