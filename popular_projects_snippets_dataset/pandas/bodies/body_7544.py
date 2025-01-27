# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reshape.py

result = idx[1:4]

# test 0th element
assert idx[0:4].equals(result.insert(0, idx[0]))
