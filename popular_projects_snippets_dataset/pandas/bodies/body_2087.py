# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# DatetimeArray
dti = date_range("1965-04-03", periods=19, freq="2W", tz=tz)
arr = DatetimeArray(dti)

result = to_datetime(arr)
assert result is arr
