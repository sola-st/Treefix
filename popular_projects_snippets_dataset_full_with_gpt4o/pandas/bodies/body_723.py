# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert lib.is_period(Period("2011-01", freq="M"))
assert not lib.is_period(PeriodIndex(["2011-01"], freq="M"))
assert not lib.is_period(Timestamp("2011-01"))
assert not lib.is_period(1)
assert not lib.is_period(np.nan)
