# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
msg = "invalid ndarray passed to infer_dtype_from_scalar"

with pytest.raises(ValueError, match=msg):
    infer_dtype_from_scalar(np.array([1]))
