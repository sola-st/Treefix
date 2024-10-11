# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant([2.0, 4.0], name="values")
i = constant_op.constant(0)
c = lambda i, *x: math_ops.less(i, 10)

# body accepts N values and returns N+1 values.
b = lambda i, *x: (i, i) + x

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    control_flow_ops.while_loop(c, b, [i, x])
