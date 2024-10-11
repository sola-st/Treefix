# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# Assert on the types resulting from Timestamp +/- various date/time
# objects
dt = datetime(2014, 3, 4)
td = timedelta(seconds=1)
ts = Timestamp(dt)

msg = "Addition/subtraction of integers"
with pytest.raises(TypeError, match=msg):
    # GH#22535 add/sub with integers is deprecated
    ts + 1
with pytest.raises(TypeError, match=msg):
    ts - 1

# Timestamp + datetime not supported, though subtraction is supported
# and yields timedelta more tests in tseries/base/tests/test_base.py
assert type(ts - dt) == Timedelta
assert type(ts + td) == Timestamp
assert type(ts - td) == Timestamp

# Timestamp +/- datetime64 not supported, so not tested (could possibly
# assert error raised?)
td64 = np.timedelta64(1, "D")
assert type(ts + td64) == Timestamp
assert type(ts - td64) == Timestamp
