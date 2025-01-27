# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_asof.py
ts = Timestamp("20130101").as_unit("ns").value
dti = DatetimeIndex([ts + 50 + i for i in range(100)])
ser = Series(np.random.randn(100), index=dti)

first_value = ser.asof(ser.index[0])

# GH#46903 previously incorrectly was "day"
assert dti.resolution == "nanosecond"

# this used to not work bc parsing was done by dateutil that didn't
#  handle nanoseconds
assert first_value == ser["2013-01-01 00:00:00.000000050"]

expected_ts = np.datetime64("2013-01-01 00:00:00.000000050", "ns")
assert first_value == ser[Timestamp(expected_ts)]
