# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
eastern, _, start, end, start_naive, end_naive = infer_setup

assert (
    timezones.infer_tzinfo(start, end)
    is conversion.localize_pydatetime(start_naive, eastern).tzinfo
)
assert (
    timezones.infer_tzinfo(start, None)
    is conversion.localize_pydatetime(start_naive, eastern).tzinfo
)
assert (
    timezones.infer_tzinfo(None, end)
    is conversion.localize_pydatetime(end_naive, eastern).tzinfo
)
