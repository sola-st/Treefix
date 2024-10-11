# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
index = simple_index
result = index.astype("O")
assert result.dtype == np.object_
