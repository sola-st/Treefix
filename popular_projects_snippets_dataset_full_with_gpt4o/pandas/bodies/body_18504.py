# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
eastern, _, _, _, start_naive, end_naive = infer_setup
msg = "Inputs must both have the same timezone"

utc = pytz.utc
start = utc.localize(start_naive)
end = conversion.localize_pydatetime(end_naive, eastern)

args = (start, end) if ordered else (end, start)

with pytest.raises(AssertionError, match=msg):
    timezones.infer_tzinfo(*args)
