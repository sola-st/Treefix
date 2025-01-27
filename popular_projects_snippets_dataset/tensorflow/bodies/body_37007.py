# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
i = constant_op.constant(0)
x = constant_op.constant([1])
c = lambda i, _: i < 10
b = lambda i, x: (i + 1, x)
with self.assertRaises((ValueError, TypeError)):
    control_flow_ops.while_loop(c, b, [i, x], ["foo", "bar"])
