# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
# GH#25777
sparray = SparseArray(arr, fill_value=fill_value)
result = sparray.sum(min_count=min_count)
if np.isnan(expected):
    assert np.isnan(result)
else:
    assert result == expected
