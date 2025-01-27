# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
ts_from_string = Timestamp("today")
ts_from_method = Timestamp.today()
ts_datetime = datetime.today()

ts_from_string_tz = Timestamp("today", tz="US/Eastern")
ts_from_method_tz = Timestamp.today(tz="US/Eastern")

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
