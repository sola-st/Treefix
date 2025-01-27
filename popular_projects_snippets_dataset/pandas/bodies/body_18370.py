# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#18831, GH#19125
box = box_with_array
xbox = np.ndarray if box is pd.array else box
td = Timedelta("5m3s")  # i.e. (scalar_td - 1sec) / 2

td1 = Series([td, td, NaT], dtype="m8[ns]")
td1 = tm.box_expected(td1, box, transpose=False)

expected = Series([0, 0, np.nan])
expected = tm.box_expected(expected, xbox, transpose=False)

result = td1 // scalar_td
tm.assert_equal(result, expected)

# Reversed op
expected = Series([2, 2, np.nan])
expected = tm.box_expected(expected, xbox, transpose=False)

result = scalar_td // td1
tm.assert_equal(result, expected)

# same thing buts let's be explicit about calling __rfloordiv__
result = td1.__rfloordiv__(scalar_td)
tm.assert_equal(result, expected)
