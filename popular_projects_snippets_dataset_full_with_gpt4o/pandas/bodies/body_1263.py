# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexers.py
with pytest.raises(IndexError, match="indices are out"):
    validate_indices(np.array([0, 1]), 0)
