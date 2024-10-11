# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#18824
tdi = TimedeltaIndex(["1 days 00:00:00", "3 days 04:00:00"])
tdi = tm.box_expected(tdi, box_with_array)

anchored = obox([offsets.MonthEnd(), offsets.Day(n=2)])

# addition/subtraction ops with anchored offsets should issue
# a PerformanceWarning and _then_ raise a TypeError.
msg = "has incorrect type|cannot add the type MonthEnd"
with pytest.raises(TypeError, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        tdi + anchored
with pytest.raises(TypeError, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        anchored + tdi
with pytest.raises(TypeError, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        tdi - anchored
with pytest.raises(TypeError, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        anchored - tdi
