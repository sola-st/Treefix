# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#47018 adapted old doctest with new behavior
d1 = datetime(2020, 1, 1, 17, tzinfo=timezone(-timedelta(hours=1)))
d2 = datetime(2020, 1, 1, 18, tzinfo=timezone(-timedelta(hours=1)))
res = to_datetime(["2020-01-01 17:00 -0100", d2])
expected = to_datetime([d1, d2]).tz_convert(timezone(timedelta(minutes=-60)))
tm.assert_index_equal(res, expected)
