# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# check that all rounding modes are accurate to int64 precision
# see GH#22591
dt = Timestamp(timestamp).as_unit("ns")
unit = to_offset(freq).nanos

# test floor
result = dt.floor(freq)
assert result.value % unit == 0, f"floor not a {freq} multiple"
assert 0 <= dt.value - result.value < unit, "floor error"

# test ceil
result = dt.ceil(freq)
assert result.value % unit == 0, f"ceil not a {freq} multiple"
assert 0 <= result.value - dt.value < unit, "ceil error"

# test round
result = dt.round(freq)
assert result.value % unit == 0, f"round not a {freq} multiple"
assert abs(result.value - dt.value) <= unit // 2, "round error"
if unit % 2 == 0 and abs(result.value - dt.value) == unit // 2:
    # round half to even
    assert result.value // unit % 2 == 0, "round half to even error"
