# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
one_us = np.timedelta64(1).astype("timedelta64[us]")

# By definition we can't go out of bounds in [ns], so we
# convert the datetime64s to [us] so we can go out of bounds
min_ts_us = np.datetime64(Timestamp.min).astype("M8[us]") + one_us
max_ts_us = np.datetime64(Timestamp.max).astype("M8[us]")

# No error for the min/max datetimes
Timestamp(min_ts_us)
Timestamp(max_ts_us)

# We used to raise on these before supporting non-nano
us_val = NpyDatetimeUnit.NPY_FR_us.value
assert Timestamp(min_ts_us - one_us)._creso == us_val
assert Timestamp(max_ts_us + one_us)._creso == us_val

# https://github.com/numpy/numpy/issues/22346 for why
#  we can't use the same construction as above with minute resolution

# too_low, too_high are the _just_ outside the range of M8[s]
too_low = np.datetime64("-292277022657-01-27T08:29", "m")
too_high = np.datetime64("292277026596-12-04T15:31", "m")

msg = "Out of bounds"
# One us less than the minimum is an error
with pytest.raises(ValueError, match=msg):
    Timestamp(too_low)

# One us more than the maximum is an error
with pytest.raises(ValueError, match=msg):
    Timestamp(too_high)
