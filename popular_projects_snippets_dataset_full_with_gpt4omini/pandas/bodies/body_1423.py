# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# label, index, slice
lbl_one, idx_one, slice_one = list("bcd"), [1, 2, 3], slice(1, 4)
lbl_two, idx_two, slice_two = ["joe", "jolie"], [1, 2], slice(1, 3)

left = df.copy()
left.loc[lbl_one, lbl_two] = rhs
tm.assert_frame_equal(left, right_loc)

left = df.copy()
left.iloc[idx_one, idx_two] = rhs
tm.assert_frame_equal(left, right_iloc)

left = df.copy()
left.iloc[slice_one, slice_two] = rhs
tm.assert_frame_equal(left, right_iloc)
