# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexers.py
indices = np.asarray([0, 1])
validate_indices(indices, 2)
validate_indices(indices[:0], 0)
validate_indices(np.array([-1, -1]), 0)
