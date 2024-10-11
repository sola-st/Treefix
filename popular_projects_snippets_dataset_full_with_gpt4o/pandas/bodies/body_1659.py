# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
left, right = left_right

out = merge(left, right, how="outer")
out.sort_values(out.columns.tolist(), inplace=True)
out.index = np.arange(len(out))
tm.assert_frame_equal(out, merge(left, right, how=how, sort=True))
