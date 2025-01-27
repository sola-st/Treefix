# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# as of 2.0, these no longer infer datetime64 based on the strings,
#  matching the Index behavior

ser = Series([None, NaT, "2013-08-05 15:30:00.000001"])
assert ser.dtype == object

ser = Series([np.nan, NaT, "2013-08-05 15:30:00.000001"])
assert ser.dtype == object

ser = Series([NaT, None, "2013-08-05 15:30:00.000001"])
assert ser.dtype == object

ser = Series([NaT, np.nan, "2013-08-05 15:30:00.000001"])
assert ser.dtype == object
