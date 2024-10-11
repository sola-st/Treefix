# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
arr = SparseArray([True, False, True], fill_value=False, dtype=np.bool_)
msg = "fill_value must be a scalar"

with pytest.raises(ValueError, match=msg):
    arr.fill_value = val
