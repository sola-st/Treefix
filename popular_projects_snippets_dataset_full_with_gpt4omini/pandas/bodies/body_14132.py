# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH19030
# Check that high-precision time values for the end of day are
# included in repr for DatetimeIndex
s1 = Series(date_range(start=start_date, freq="D", periods=5))
result = str(s1)
assert start_date in result

dti = date_range(start=start_date, freq="D", periods=5)
s2 = Series(3, index=dti)
result = str(s2.index)
assert start_date in result
