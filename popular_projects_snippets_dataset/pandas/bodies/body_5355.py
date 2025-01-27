# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
ts = Timestamp("2014-11-02 01:00")
ts_dst = ts.tz_localize("US/Eastern", ambiguous=True)
ts_no_dst = ts.tz_localize("US/Eastern", ambiguous=False)

assert ts_no_dst.value - ts_dst.value == 3600
msg = re.escape(
    "'ambiguous' parameter must be one of: "
    "True, False, 'NaT', 'raise' (default)"
)
with pytest.raises(ValueError, match=msg):
    ts.tz_localize("US/Eastern", ambiguous="infer")

# GH#8025
msg = "Cannot localize tz-aware Timestamp, use tz_convert for conversions"
with pytest.raises(TypeError, match=msg):
    Timestamp("2011-01-01", tz="US/Eastern").tz_localize("Asia/Tokyo")

msg = "Cannot convert tz-naive Timestamp, use tz_localize to localize"
with pytest.raises(TypeError, match=msg):
    Timestamp("2011-01-01").tz_convert("Asia/Tokyo")
