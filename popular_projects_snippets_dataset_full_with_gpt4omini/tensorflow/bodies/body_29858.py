# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
for dtype in [
    dtypes_lib.half, dtypes_lib.float32, dtypes_lib.float64,
    dtypes_lib.int8, dtypes_lib.uint8, dtypes_lib.int16, dtypes_lib.uint16,
    dtypes_lib.int32, dtypes_lib.int64, dtypes_lib.bool,
    dtypes_lib.complex64, dtypes_lib.complex128, dtypes_lib.string
]:
    self._compareZeros(dtype, fully_defined_shape=False, use_gpu=False)
    self._compareZeros(dtype, fully_defined_shape=True, use_gpu=False)
