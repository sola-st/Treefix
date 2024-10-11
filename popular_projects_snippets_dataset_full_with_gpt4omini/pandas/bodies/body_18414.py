# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
box = box_with_array

left = Series(data, dtype=dtype)
left = tm.box_expected(left, box)
xbox = get_upcast_box(left, NaT, True)

expected = [False, False, False]
expected = tm.box_expected(expected, xbox)
if box is pd.array and dtype is object:
    expected = pd.array(expected, dtype="bool")

tm.assert_equal(left == NaT, expected)
tm.assert_equal(NaT == left, expected)

expected = [True, True, True]
expected = tm.box_expected(expected, xbox)
if box is pd.array and dtype is object:
    expected = pd.array(expected, dtype="bool")
tm.assert_equal(left != NaT, expected)
tm.assert_equal(NaT != left, expected)

expected = [False, False, False]
expected = tm.box_expected(expected, xbox)
if box is pd.array and dtype is object:
    expected = pd.array(expected, dtype="bool")
tm.assert_equal(left < NaT, expected)
tm.assert_equal(NaT > left, expected)
tm.assert_equal(left <= NaT, expected)
tm.assert_equal(NaT >= left, expected)

tm.assert_equal(left > NaT, expected)
tm.assert_equal(NaT < left, expected)
tm.assert_equal(left >= NaT, expected)
tm.assert_equal(NaT <= left, expected)
