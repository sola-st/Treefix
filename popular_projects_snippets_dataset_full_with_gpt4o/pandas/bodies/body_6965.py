# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#38743
if index.empty:
    # No duplicates in empty indexes
    exit()

idx = index
idx_non_unique = idx[[0, 0, 1, 2]]

assert idx.intersection(idx_non_unique).equals(idx_non_unique.intersection(idx))
assert idx.intersection(idx_non_unique).is_unique
