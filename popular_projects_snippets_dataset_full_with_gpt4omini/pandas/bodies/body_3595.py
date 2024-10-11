# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
result = obj.dot(other.iloc[::-1]["1"])
self.reduced_dim_assert(result, expected["1"])
