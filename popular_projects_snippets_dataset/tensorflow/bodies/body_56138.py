# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
for dtype in [
    dtypes.float32, dtypes.float64, dtypes.bool, dtypes.uint8, dtypes.int8,
    dtypes.int16, dtypes.int32, dtypes.int64, dtypes.float8_e5m2,
    dtypes.float8_e4m3fn
]:
    self.assertIs(dtype.real_dtype, dtype)
self.assertIs(dtypes.complex64.real_dtype, dtypes.float32)
self.assertIs(dtypes.complex128.real_dtype, dtypes.float64)
