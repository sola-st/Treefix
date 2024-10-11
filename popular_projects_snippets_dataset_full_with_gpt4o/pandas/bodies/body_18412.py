# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22242, GH#22163 DataFrame considered NaT == ts incorrectly
tz = tz_naive_fixture
box = box_with_array

ts = Timestamp("2021-01-01", tz=tz)
ser = Series([ts, NaT])

obj = tm.box_expected(ser, box)
xbox = get_upcast_box(obj, ts, True)

expected = Series([True, False], dtype=np.bool_)
expected = tm.box_expected(expected, xbox)

result = obj == ts
tm.assert_equal(result, expected)
