# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index = simple_index
result = index.astype("O")
assert result.dtype == np.object_
