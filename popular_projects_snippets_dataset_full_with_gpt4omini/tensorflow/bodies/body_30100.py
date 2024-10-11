# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for dtype in [
    np.uint8, np.int8, np.uint16, np.int16, np.uint32, np.int32, np.uint64,
    np.int64, np.bool_, np.float16, np.float32, np.float64, np.complex64,
    np.complex128,
    np.array(b"").dtype.type, dtypes.bfloat16.as_numpy_dtype
]:
    self._reverse2DimAuto(dtype)
