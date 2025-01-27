# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# MultiIndex is tested separately
index = index_flat
if isinstance(index, RangeIndex):
    pytest.skip(
        "RangeIndex is tested in test_drop_duplicates_no_duplicates "
        "as it cannot hold duplicates"
    )
if len(index) == 0:
    pytest.skip(
        "empty index is tested in test_drop_duplicates_no_duplicates "
        "as it cannot hold duplicates"
    )

# make unique index
holder = type(index)
unique_values = list(set(index))
dtype = index.dtype if isinstance(index, NumericIndex) else None
unique_idx = holder(unique_values, dtype=dtype)

# make duplicated index
n = len(unique_idx)
duplicated_selection = np.random.choice(n, int(n * 1.5))
idx = holder(unique_idx.values[duplicated_selection])

# Series.duplicated is tested separately
expected_duplicated = (
    pd.Series(duplicated_selection).duplicated(keep=keep).values
)
tm.assert_numpy_array_equal(idx.duplicated(keep=keep), expected_duplicated)

# Series.drop_duplicates is tested separately
expected_dropped = holder(pd.Series(idx).drop_duplicates(keep=keep))
tm.assert_index_equal(idx.drop_duplicates(keep=keep), expected_dropped)
