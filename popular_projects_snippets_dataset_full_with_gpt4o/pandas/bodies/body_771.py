# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
# to trigger the motivating bug, the first N elements of the arrays need
#  to match
first = np.array([1, 2, 3])
second = np.array([1, 2])

left = Series([first, "a"], dtype=object)
right = Series([second, "a"], dtype=object)
assert not array_equivalent(left, right)
