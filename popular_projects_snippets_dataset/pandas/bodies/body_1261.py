# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexers.py
indices = np.asarray([0, -2])
with pytest.raises(ValueError, match="'indices' contains"):
    validate_indices(indices, 2)
