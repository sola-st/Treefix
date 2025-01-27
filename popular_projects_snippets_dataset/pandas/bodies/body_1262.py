# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexers.py
indices = np.asarray([0, 1, 2])
with pytest.raises(IndexError, match="indices are out"):
    validate_indices(indices, 2)
