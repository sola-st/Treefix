# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#19042 test for correct name attachment
box = box_with_array
exname = get_expected_name(box, names)

tdi = TimedeltaIndex(
    ["0days", "1day", "2days", "3days", "4days"], name=names[0]
)
# TODO: Should we be parametrizing over types for `ser` too?
ser = Series([0, 1, 2, 3, 4], dtype=np.int64, name=names[1])

expected = Series(
    ["0days", "1day", "4days", "9days", "16days"],
    dtype="timedelta64[ns]",
    name=exname,
)

tdi = tm.box_expected(tdi, box)
xbox = get_upcast_box(tdi, ser)

expected = tm.box_expected(expected, xbox)

result = ser * tdi
tm.assert_equal(result, expected)

result = tdi * ser
tm.assert_equal(result, expected)
