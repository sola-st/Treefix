# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# regression test for GH#5963
box = box_with_array
xbox = box if box not in [pd.Index, pd.array] else np.ndarray

ser = Series([timedelta(days=1), timedelta(days=2)])
ser = tm.box_expected(ser, box)
actual = ser > td_scalar
expected = Series([False, True])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(actual, expected)
