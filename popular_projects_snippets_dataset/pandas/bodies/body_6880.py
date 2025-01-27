# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# MultiIndex is tested separately
index = index_flat

# make unique index
if isinstance(index, RangeIndex):
    # RangeIndex cannot have duplicates
    unique_idx = index
else:
    holder = type(index)
    unique_values = list(set(index))
    dtype = index.dtype if isinstance(index, NumericIndex) else None
    unique_idx = holder(unique_values, dtype=dtype)

# check on unique index
expected_duplicated = np.array([False] * len(unique_idx), dtype="bool")
tm.assert_numpy_array_equal(unique_idx.duplicated(), expected_duplicated)
result_dropped = unique_idx.drop_duplicates()
tm.assert_index_equal(result_dropped, unique_idx)
# validate shallow copy
assert result_dropped is not unique_idx
