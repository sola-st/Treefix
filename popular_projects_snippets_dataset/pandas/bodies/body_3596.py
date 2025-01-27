# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
# Check index alignment
other2 = other.iloc[::-1]
result = obj.dot(other2)
tm.assert_equal(result, expected)
