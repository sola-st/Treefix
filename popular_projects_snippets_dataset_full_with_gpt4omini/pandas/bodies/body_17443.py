# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py

if normalize and issubclass(offset, Tick):
    # normalize=True disallowed for Tick subclasses GH#21427
    exit()

offset_s = _create_offset(offset, normalize=normalize)
func = getattr(offset_s, funcname)

result = func(dt)
assert isinstance(result, Timestamp)
assert result == expected

result = func(Timestamp(dt))
assert isinstance(result, Timestamp)
assert result == expected

# see gh-14101
exp_warning = None
ts = Timestamp(dt) + Nano(5)

if (
    type(offset_s).__name__ == "DateOffset"
    and (funcname in ["apply", "_apply"] or normalize)
    and ts.nanosecond > 0
):
    exp_warning = UserWarning

# test nanosecond is preserved
with tm.assert_produces_warning(exp_warning):
    result = func(ts)

assert isinstance(result, Timestamp)
if normalize is False:
    assert result == expected + Nano(5)
else:
    assert result == expected

if isinstance(dt, np.datetime64):
    # test tz when input is datetime or Timestamp
    exit()

for tz in [
    None,
    "UTC",
    "Asia/Tokyo",
    "US/Eastern",
    "dateutil/Asia/Tokyo",
    "dateutil/US/Pacific",
]:
    expected_localize = expected.tz_localize(tz)
    tz_obj = timezones.maybe_get_tz(tz)
    dt_tz = conversion.localize_pydatetime(dt, tz_obj)

    result = func(dt_tz)
    assert isinstance(result, Timestamp)
    assert result == expected_localize

    result = func(Timestamp(dt, tz=tz))
    assert isinstance(result, Timestamp)
    assert result == expected_localize

    # see gh-14101
    exp_warning = None
    ts = Timestamp(dt, tz=tz) + Nano(5)

    if (
        type(offset_s).__name__ == "DateOffset"
        and (funcname in ["apply", "_apply"] or normalize)
        and ts.nanosecond > 0
    ):
        exp_warning = UserWarning

    # test nanosecond is preserved
    with tm.assert_produces_warning(exp_warning):
        result = func(ts)
    assert isinstance(result, Timestamp)
    if normalize is False:
        assert result == expected_localize + Nano(5)
    else:
        assert result == expected_localize
