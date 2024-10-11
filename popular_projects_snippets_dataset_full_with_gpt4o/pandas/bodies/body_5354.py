# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# make sure that we are correctly accepting bool values as ambiguous
# GH#14402
ts = Timestamp("2015-11-01 01:00:03").as_unit(unit)
expected0 = Timestamp("2015-11-01 01:00:03-0500", tz="US/Central")
expected1 = Timestamp("2015-11-01 01:00:03-0600", tz="US/Central")

msg = "Cannot infer dst time from 2015-11-01 01:00:03"
with pytest.raises(pytz.AmbiguousTimeError, match=msg):
    ts.tz_localize("US/Central")

with pytest.raises(pytz.AmbiguousTimeError, match=msg):
    ts.tz_localize("dateutil/US/Central")

if ZoneInfo is not None:
    try:
        tz = ZoneInfo("US/Central")
    except KeyError:
        # no tzdata
        pass
    else:
        with pytest.raises(pytz.AmbiguousTimeError, match=msg):
            ts.tz_localize(tz)

result = ts.tz_localize("US/Central", ambiguous=True)
assert result == expected0
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value

result = ts.tz_localize("US/Central", ambiguous=False)
assert result == expected1
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value
