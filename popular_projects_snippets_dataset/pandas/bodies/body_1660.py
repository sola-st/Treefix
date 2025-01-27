# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
left, right = left_right

# check that left merge w/ sort=False maintains left frame order
out = merge(left, right, how="left", sort=False)
tm.assert_frame_equal(left, out[left.columns.tolist()])

out = merge(right, left, how="left", sort=False)
tm.assert_frame_equal(right, out[right.columns.tolist()])
