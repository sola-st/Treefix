# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# Test comparison with zero-dimensional array is unboxed
tz = tz_naive_fixture
box = box_with_array
dti = date_range("20130101", periods=3, tz=tz)

other = np.array(dti.to_numpy()[0])

dtarr = tm.box_expected(dti, box)
xbox = get_upcast_box(dtarr, other, True)
result = dtarr <= other
expected = np.array([True, False, False])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(result, expected)
