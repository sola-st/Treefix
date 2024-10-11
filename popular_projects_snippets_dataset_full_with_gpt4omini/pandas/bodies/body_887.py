# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
pi = period_range("2016", periods=3, freq="A")

elem = element(pi)
self.check_series_setitem(elem, pi, True)

# Careful: to get the expected Series-inplace behavior we need
# `elem` to not have the same length as `arr`
pi2 = pi.asfreq("D")[:-1]
elem = element(pi2)
self.check_series_setitem(elem, pi, False)

dti = pi.to_timestamp("S")[:-1]
elem = element(dti)
self.check_series_setitem(elem, pi, False)
