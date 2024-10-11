# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# GH#22085
dtype = any_real_numpy_dtype
data = [0, 1, 2, 3] if not is_float_dtype(dtype) else [0.1, 1.1, 2.2, 3.3]
index = NumericIndex(data, dtype=dtype)

if not is_float_dtype(index.dtype):
    assert 1.1 not in index
    assert 1.0 in index
    assert 1 in index
else:
    assert 1.1 in index
    assert 1.0 not in index
    assert 1 not in index
