# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
exp_idx = idx[[2, 3]]
expected = Series([3, 2], index=exp_idx)

for obj in [idx, Series(idx)]:
    tm.assert_series_equal(obj.value_counts(), expected)

exp_idx = idx[[2, 3, -1]]
expected = Series([3, 2, 1], index=exp_idx)

for obj in [idx, Series(idx)]:
    tm.assert_series_equal(obj.value_counts(dropna=False), expected)

tm.assert_index_equal(idx.unique(), exp_idx)
