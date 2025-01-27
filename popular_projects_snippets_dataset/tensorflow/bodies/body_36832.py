# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant(1.0)
b = control_flow_ops.cond(
    constant_op.constant(True), lambda: math_ops.square(x),
    lambda: math_ops.subtract(x, 1.))
self.assertEqual(b.shape, tensor_shape.TensorShape([]))
