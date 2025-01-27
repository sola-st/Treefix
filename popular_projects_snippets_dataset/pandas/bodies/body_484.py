# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
a = PeriodDtype("period[D]")
b = PeriodDtype("period[3D]")

assert issubclass(type(a), type(a))
assert issubclass(type(a), type(b))
