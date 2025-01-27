# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
pi = period_range("2000-01-01", periods=10, freq="D")

val = pi[3]
expected = [x > val for x in pi]

ser = tm.box_expected(pi, box_with_array)
xbox = get_upcast_box(ser, val, True)

expected = tm.box_expected(expected, xbox)
result = ser > val
tm.assert_equal(result, expected)

val = pi[5]
result = ser > val
expected = [x > val for x in pi]
expected = tm.box_expected(expected, xbox)
tm.assert_equal(result, expected)
