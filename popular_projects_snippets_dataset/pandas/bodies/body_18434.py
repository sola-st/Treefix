# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
t1 = date_range("20130101", periods=3).tz_localize("US/Eastern")
t1 = tm.box_expected(t1, box_with_array)
t2 = date_range("20130101", periods=3).tz_localize("CET")
t2 = tm.box_expected(t2, box_with_array)
tnaive = date_range("20130101", periods=3)

result = t1 - t2
expected = TimedeltaIndex(
    ["0 days 06:00:00", "0 days 06:00:00", "0 days 06:00:00"]
)
expected = tm.box_expected(expected, box_with_array)
tm.assert_equal(result, expected)

result = t2 - t1
expected = TimedeltaIndex(
    ["-1 days +18:00:00", "-1 days +18:00:00", "-1 days +18:00:00"]
)
expected = tm.box_expected(expected, box_with_array)
tm.assert_equal(result, expected)

msg = "Cannot subtract tz-naive and tz-aware datetime-like objects"
with pytest.raises(TypeError, match=msg):
    t1 - tnaive

with pytest.raises(TypeError, match=msg):
    tnaive - t1
