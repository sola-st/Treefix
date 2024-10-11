# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
# Check series argument
result = obj.dot(other["1"])
self.reduced_dim_assert(result, expected["1"])
