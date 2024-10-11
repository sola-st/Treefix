# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# scalar
assert idx[2] == ("bar", "one")

# slice
result = idx[2:5]
expected = idx[[2, 3, 4]]
assert result.equals(expected)

# boolean
result = idx[[True, False, True, False, True, True]]
result2 = idx[np.array([True, False, True, False, True, True])]
expected = idx[[0, 2, 4, 5]]
assert result.equals(expected)
assert result2.equals(expected)
