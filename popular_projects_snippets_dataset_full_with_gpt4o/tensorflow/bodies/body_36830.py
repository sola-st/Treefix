# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
values = constant_op.constant(10)
fn1 = lambda: math_ops.add(values, 1)
fn2 = lambda: math_ops.subtract(values, 1)
with self.assertRaisesRegex(TypeError, "must not be a Python bool"):
    _ = control_flow_ops.cond(False, fn1, fn2)
