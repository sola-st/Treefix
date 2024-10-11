# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
# Check ndarray argument; in this case we get matching values,
#  but index/columns may not match
result = obj.dot(other.values)
assert np.all(result == expected.values)
