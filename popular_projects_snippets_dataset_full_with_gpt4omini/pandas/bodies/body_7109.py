# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
result = index[1:4]

if not len(index):
    exit()

# test 0th element
assert index[0:4].equals(result.insert(0, index[0]))
