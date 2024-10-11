# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
_, _, start, end, start_naive, end_naive = infer_setup
utc = pytz.utc

start = utc.localize(start_naive)
end = utc.localize(end_naive)

assert timezones.infer_tzinfo(start, end) is utc
