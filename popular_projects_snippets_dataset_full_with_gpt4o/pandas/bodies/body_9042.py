# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
zarr = SparseArray([0, 0, 1, 2, 3, 0, 4, 5, 0, 6], fill_value=0)

assert np.isnan(arr[1])
assert arr[2] == 1
assert arr[7] == 5

assert zarr[0] == 0
assert zarr[2] == 1
assert zarr[7] == 5

errmsg = "must be an integer between -10 and 10"

with pytest.raises(IndexError, match=errmsg):
    arr[11]

with pytest.raises(IndexError, match=errmsg):
    arr[-11]

assert arr[-1] == arr[len(arr) - 1]
