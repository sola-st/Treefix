# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#42288, GH#24559
dt = np.datetime64("1970-01-01 05:00:00")
tzstr = "UTC+05:00"

# pre-2.0 this interpreted dt as a UTC time. in 2.0 this is treated
#  as a wall-time, consistent with DatetimeIndex behavior
ts = Timestamp(dt, tz=tzstr)

alt = Timestamp(dt).tz_localize(tzstr)
assert ts == alt
assert ts.hour == 5
