# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
dt = date_range(start=start, freq=index_freq, periods=periods)
unit = to_offset(round_freq).nanos

# test floor
result = dt.floor(round_freq)
diff = dt.asi8 - result.asi8
mod = result.asi8 % unit
assert (mod == 0).all(), f"floor not a {round_freq} multiple"
assert (0 <= diff).all() and (diff < unit).all(), "floor error"

# test ceil
result = dt.ceil(round_freq)
diff = result.asi8 - dt.asi8
mod = result.asi8 % unit
assert (mod == 0).all(), f"ceil not a {round_freq} multiple"
assert (0 <= diff).all() and (diff < unit).all(), "ceil error"

# test round
result = dt.round(round_freq)
diff = abs(result.asi8 - dt.asi8)
mod = result.asi8 % unit
assert (mod == 0).all(), f"round not a {round_freq} multiple"
assert (diff <= unit // 2).all(), "round error"
if unit % 2 == 0:
    assert (
        result.asi8[diff == unit // 2] % 2 == 0
    ).all(), "round half to even error"
