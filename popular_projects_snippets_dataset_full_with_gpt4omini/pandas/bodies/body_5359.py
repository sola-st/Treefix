# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
tz = tz_aware_fixture
ts = Timestamp(stamp)
localized = ts.tz_localize(tz)
assert localized == Timestamp(stamp, tz=tz)

msg = "Cannot localize tz-aware Timestamp"
with pytest.raises(TypeError, match=msg):
    localized.tz_localize(tz)

reset = localized.tz_localize(None)
assert reset == ts
assert reset.tzinfo is None
