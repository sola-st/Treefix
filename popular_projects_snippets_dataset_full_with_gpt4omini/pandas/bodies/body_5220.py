# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# GH 12690
result = Timedelta(value, unit=unit)
assert result.value == expected
result = Timedelta(str(value) + unit)
assert result.value == expected
