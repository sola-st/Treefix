# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
for dtype in [
    dtypes_lib.float32, dtypes_lib.float64, dtypes_lib.int32,
    dtypes_lib.bool, dtypes_lib.int64,
    # TODO(josh11b): Support string type here.
    # dtypes_lib.string
]:
    self._compareZeros(dtype, use_gpu=True)
