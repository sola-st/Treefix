# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# GH#21282
result = index[...]
assert result.equals(index)
assert result is not index
