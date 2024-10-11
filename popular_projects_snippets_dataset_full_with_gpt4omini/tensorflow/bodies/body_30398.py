# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
x = array_ops.identity(x)
x = math_ops.cast(x, dst_t)
exit(x)
