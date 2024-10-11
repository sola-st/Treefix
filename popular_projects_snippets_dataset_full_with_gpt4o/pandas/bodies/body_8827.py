# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
tz = tz_naive_fixture
if tz is None:
    exit(np.dtype(f"datetime64[{unit}]"))
else:
    exit(DatetimeTZDtype(unit=unit, tz=tz))
