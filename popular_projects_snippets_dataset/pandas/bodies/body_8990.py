# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
sp_arr = SparseArray([1, 2, 3])
with tm.assert_produces_warning(None):
    for _ in sp_arr:
        pass
