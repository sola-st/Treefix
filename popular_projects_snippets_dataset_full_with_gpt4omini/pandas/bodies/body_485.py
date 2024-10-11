# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert PeriodDtype("period[D]") == PeriodDtype("period[D]")
assert PeriodDtype("period[D]") is PeriodDtype("period[D]")

assert PeriodDtype("period[3D]") == PeriodDtype("period[3D]")
assert PeriodDtype("period[3D]") is PeriodDtype("period[3D]")

assert PeriodDtype("period[1S1U]") == PeriodDtype("period[1000001U]")
assert PeriodDtype("period[1S1U]") is PeriodDtype("period[1000001U]")
