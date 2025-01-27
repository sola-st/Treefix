# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#26689 make sure we unbox zero-dimensional arrays

pi = period_range("2000", periods=4)
other = np.array(pi.to_numpy()[0])

pi = tm.box_expected(pi, box_with_array)
xbox = get_upcast_box(pi, other, True)

result = pi <= other
expected = np.array([True, False, False, False])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(result, expected)
