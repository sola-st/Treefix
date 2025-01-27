# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# https://github.com/pandas-dev/pandas/issues/37265
dtype = PeriodDtype(freq="M")
assert (dtype == "period[M]") is True
assert (dtype != "period[M]") is False
