# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(range(5))
result = index.groupby(np.array([1, 1, 2, 2, 2]))
expected = {1: Index([0, 1]), 2: Index([2, 3, 4])}

tm.assert_dict_equal(result, expected)
