# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant([2.0, 4.0], name="values")
i = constant_op.constant(0)
c = lambda i, _: math_ops.less(i, 10)
b = lambda i, x: [i + 1, x + 1]
with self.assertRaisesRegex(ValueError, "is not compatible with"):
    # Shape of x is [2], but we specify a shape of [5].
    control_flow_ops.while_loop(
        c, b, [i, x], [i.shape, tensor_shape.TensorShape([5])])
