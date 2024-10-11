# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH#20439
cat = Categorical([(0, 1), (0, 2), (0, 1)])

# This should not raise
cat[1] = cat[0]
assert cat[1] == (0, 1)
