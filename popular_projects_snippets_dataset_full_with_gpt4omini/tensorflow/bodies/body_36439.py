# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [4], [5, 6]])
x_spec = type_spec.type_spec_from_value(x)
y, = script_ops.eager_py_func(lambda v: v, [x], [x_spec])
self.assertAllEqual(y, x)
