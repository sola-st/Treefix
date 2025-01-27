# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#18849, GH#19744
box = box_with_array
exname = get_expected_name(box, names)

tdi = TimedeltaIndex(["1 days 00:00:00", "3 days 04:00:00"], name=names[0])
other = pd.Index([offsets.Hour(n=1), offsets.Minute(n=-2)], name=names[1])
other = np.array(other) if box in [tm.to_array, pd.array] else other

expected = TimedeltaIndex(
    [tdi[n] + other[n] for n in range(len(tdi))], freq="infer", name=exname
)
expected_sub = TimedeltaIndex(
    [tdi[n] - other[n] for n in range(len(tdi))], freq="infer", name=exname
)

tdi = tm.box_expected(tdi, box)
expected = tm.box_expected(expected, box).astype(object, copy=False)
expected_sub = tm.box_expected(expected_sub, box).astype(object, copy=False)

with tm.assert_produces_warning(PerformanceWarning):
    res = tdi + other
tm.assert_equal(res, expected)

with tm.assert_produces_warning(PerformanceWarning):
    res2 = other + tdi
tm.assert_equal(res2, expected)

with tm.assert_produces_warning(PerformanceWarning):
    res_sub = tdi - other
tm.assert_equal(res_sub, expected_sub)
