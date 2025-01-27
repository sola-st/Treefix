# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
# GH#33856 shifting with periods=0 should return a copy, not same obj
result = data.shift(0)

data._sparse_values[0] = data._sparse_values[1]
assert result._sparse_values[0] != result._sparse_values[1]
