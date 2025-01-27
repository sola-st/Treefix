# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_rendering.py
# avoid to match with timezone name
freq_repr = f"'{freq}'"
if tz.startswith("dateutil"):
    tz_repr = tz.replace("dateutil", "")
else:
    tz_repr = tz

date_only = Timestamp(date)
assert date in repr(date_only)
assert tz_repr not in repr(date_only)
assert freq_repr not in repr(date_only)
assert date_only == eval(repr(date_only))

date_tz = Timestamp(date, tz=tz)
assert date in repr(date_tz)
assert tz_repr in repr(date_tz)
assert freq_repr not in repr(date_tz)
assert date_tz == eval(repr(date_tz))
