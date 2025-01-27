# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 17537
grouped = mframe.groupby(level=0, sort=sort)
exp_labels = np.array(labels, np.intp)
tm.assert_almost_equal(grouped.grouper.codes[0], exp_labels)
