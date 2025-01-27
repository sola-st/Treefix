# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH 24713
tz = pytz.timezone("US/Eastern")
dr = date_range("2013-01-01", periods=3, tz="US/Eastern")
dtype = DatetimeTZDtype("ns", dr.tz)
assert dtype.tz == tz
dtype = DatetimeTZDtype("ns", dr[0].tz)
assert dtype.tz == tz
