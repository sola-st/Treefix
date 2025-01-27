# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
exit(math_ops.cast(
    array_ops.ones([2, 3], dtype=dtypes_lib.quint8), dtypes_lib.int32))
