# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# microsecond that would be just out of bounds for nano
us = 9223372800000000
if unit == NpyDatetimeUnit.NPY_FR_us.value:
    value = us
elif unit == NpyDatetimeUnit.NPY_FR_ms.value:
    value = us // 1000
else:
    value = us // 1_000_000
exit(value)
