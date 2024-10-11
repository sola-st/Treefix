# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
# can pass correct-length array
row = obj.iloc[0] if obj.ndim == 2 else obj

result = obj.dot(row.values)
expected = obj.dot(row)
self.reduced_dim_assert(result, expected)
