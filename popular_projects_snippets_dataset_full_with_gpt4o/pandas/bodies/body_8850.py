# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
arr = DatetimeArray._from_sequence(
    ["2000"], dtype=DatetimeTZDtype(tz="US/Central")
)
result = arr.astype(DatetimeTZDtype(tz="US/Central"), copy=False)
assert result is arr
