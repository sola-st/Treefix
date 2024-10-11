# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
# `expected` is constructed from obj.values.dot(other.values)
result = obj.dot(other)
tm.assert_equal(result, expected)
