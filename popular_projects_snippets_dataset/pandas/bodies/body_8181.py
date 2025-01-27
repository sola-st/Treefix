# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# note: this tz tests that a tz-naive index can be localized
# and de-localized successfully, when there are no DST transitions
# in the range.
idx = date_range(start="2014-06-01", end="2014-08-30", freq="15T")
tz = tz_aware_fixture
localized = idx.tz_localize(tz)
# can't localize a tz-aware object
with pytest.raises(
    TypeError, match="Already tz-aware, use tz_convert to convert"
):
    localized.tz_localize(tz)
reset = localized.tz_localize(None)
assert reset.tzinfo is None
expected = idx._with_freq(None)
tm.assert_index_equal(reset, expected)
