# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [4], [5, 6]])
y, = script_ops.eager_py_func(math_ops.reduce_sum, [x], [dtypes.int32])
self.assertAllEqual(y, 21)
