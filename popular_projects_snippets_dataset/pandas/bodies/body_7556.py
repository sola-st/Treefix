# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py
groups = idx.groupby(np.array([1, 1, 1, 2, 2, 2]))
labels = idx.tolist()
exp = {1: labels[:3], 2: labels[3:]}
tm.assert_dict_equal(groups, exp)

# GH5620
groups = idx.groupby(idx)
exp = {key: [key] for key in idx}
tm.assert_dict_equal(groups, exp)
