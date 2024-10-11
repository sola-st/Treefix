# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
Inf = libalgos.Infinity()
NegInf = libalgos.NegInfinity()

assert not Inf > np.nan
assert not Inf >= np.nan
assert not Inf < np.nan
assert not Inf <= np.nan
assert not Inf == np.nan
assert Inf != np.nan

assert not NegInf > np.nan
assert not NegInf >= np.nan
assert not NegInf < np.nan
assert not NegInf <= np.nan
assert not NegInf == np.nan
assert NegInf != np.nan
