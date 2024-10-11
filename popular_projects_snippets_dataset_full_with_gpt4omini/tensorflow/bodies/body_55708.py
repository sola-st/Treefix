# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
x = constant_op.constant([[1, 2, 3]])
y = script_ops.eager_py_func(lambda: [[1, 2, 3]], (), dtypes.int32)
exit(math_ops.matmul(x, y))
