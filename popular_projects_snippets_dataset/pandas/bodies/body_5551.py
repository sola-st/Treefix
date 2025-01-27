# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#9000
ts_from_string = Timestamp("now")
ts_from_method = Timestamp.now()
ts_datetime = datetime.now()

ts_from_string_tz = Timestamp("now", tz="US/Eastern")
ts_from_method_tz = Timestamp.now(tz="US/Eastern")

# Check that the delta between the times is less than 1s (arbitrarily
# small)
delta = Timedelta(seconds=1)
assert abs(ts_from_method - ts_from_string) < delta
assert abs(ts_datetime - ts_from_method) < delta
assert abs(ts_from_method_tz - ts_from_string_tz) < delta
assert (
    abs(
        ts_from_string_tz.tz_localize(None)
        - ts_from_method_tz.tz_localize(None)
    )
    < delta
)
