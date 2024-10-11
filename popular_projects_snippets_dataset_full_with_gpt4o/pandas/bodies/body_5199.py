# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# 7, 8, 9 correspond to second, millisecond, and microsecond, respectively
attr = f"NPY_FR_{unit_str}"
exit(getattr(NpyDatetimeUnit, attr).value)
