# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#33671
dti = date_range("2016-01-01", periods=10, tz="CET")
dti_utc = dti.tz_convert("UTC")
ser = Series(10, index=dti)
ser_utc = Series(10, index=dti_utc)

# we don't care about the result, just that original indexes are unchanged
ser * ser_utc

assert ser.index is dti
assert ser_utc.index is dti_utc
