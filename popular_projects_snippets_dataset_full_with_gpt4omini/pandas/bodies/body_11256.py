# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
grouped = mframe.groupby(mframe.index.get_level_values(0))
exp_labels = np.array([2, 2, 2, 0, 0, 1, 1, 3, 3, 3], dtype=np.intp)
tm.assert_almost_equal(grouped.grouper.codes[0], exp_labels)
