# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# See GH#18666
# Test with one timezone far ahead of UTC and another far behind, so
# one of these will _almost_ always be in a different day from UTC.
# Unfortunately this test between 12 and 1 AM Samoa time
# this both of these timezones _and_ UTC will all be in the same day,
# so this test will not detect the regression introduced in #18666.
with tm.set_timezone(tz):
    nptoday = np.datetime64("today").astype("datetime64[ns]").astype(np.int64)
    pdtoday = to_datetime("today")
    pdtoday2 = to_datetime(["today"])[0]

    tstoday = Timestamp("today")
    tstoday2 = Timestamp.today().as_unit("ns")

    # These should all be equal with infinite perf; this gives
    # a generous margin of 10 seconds
    assert abs(pdtoday.normalize().value - nptoday) < 1e10
    assert abs(pdtoday2.normalize().value - nptoday) < 1e10
    assert abs(pdtoday.value - tstoday.value) < 1e10
    assert abs(pdtoday.value - tstoday2.value) < 1e10

    assert pdtoday.tzinfo is None
    assert pdtoday2.tzinfo is None
