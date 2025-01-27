# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH#12677
# tz_localize that pushes away from the boundary is OK
msg = (
    f"Converting {Timestamp.min.strftime('%Y-%m-%d %H:%M:%S')} "
    f"underflows past {Timestamp.min}"
)
pac = Timestamp.min.tz_localize("US/Pacific")
assert pac.value > Timestamp.min.value
pac.tz_convert("Asia/Tokyo")  # tz_convert doesn't change value
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp.min.tz_localize("Asia/Tokyo")

# tz_localize that pushes away from the boundary is OK
msg = (
    f"Converting {Timestamp.max.strftime('%Y-%m-%d %H:%M:%S')} "
    f"overflows past {Timestamp.max}"
)
tokyo = Timestamp.max.tz_localize("Asia/Tokyo")
assert tokyo.value < Timestamp.max.value
tokyo.tz_convert("US/Pacific")  # tz_convert doesn't change value
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp.max.tz_localize("US/Pacific")
