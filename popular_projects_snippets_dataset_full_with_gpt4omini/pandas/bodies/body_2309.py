# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# see gh-7506
a = DataFrame({0: [1, 2], 1: [3, 4], 2: [5, 6]})
b = DataFrame({0: [np.nan, 8], 1: [9, np.nan], 2: [np.nan, np.nan]})
do_not_replace = b.isna() | (a > b)

expected = a.copy()
expected[~do_not_replace] = b

result = a.where(do_not_replace, b)
tm.assert_frame_equal(result, expected)

a = DataFrame({0: [4, 6], 1: [1, 0]})
b = DataFrame({0: [np.nan, 3], 1: [3, np.nan]})
do_not_replace = b.isna() | (a > b)

expected = a.copy()
expected[~do_not_replace] = b

result = a.where(do_not_replace, b)
tm.assert_frame_equal(result, expected)
