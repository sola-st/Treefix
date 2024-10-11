# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
arr = SparseArray(raw_data)
max_result = arr.max()
min_result = arr.min()
assert max_result in max_expected
assert min_result in min_expected

max_result = arr.max(skipna=False)
min_result = arr.min(skipna=False)
if np.isnan(raw_data).any():
    assert np.isnan(max_result)
    assert np.isnan(min_result)
else:
    assert max_result in max_expected
    assert min_result in min_expected
