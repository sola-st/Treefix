# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# initialize a unique index
index = simple_index.drop_duplicates()
assert index.is_unique is True

# empty index should be unique
index_empty = index[:0]
assert index_empty.is_unique is True

# test basic dupes
index_dup = index.insert(0, index[0])
assert index_dup.is_unique is False

# single NA should be unique
index_na = index.insert(0, np.nan)
assert index_na.is_unique is True

# multiple NA should not be unique
index_na_dup = index_na.insert(0, np.nan)
assert index_na_dup.is_unique is False
