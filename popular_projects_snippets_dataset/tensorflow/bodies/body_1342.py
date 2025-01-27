# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
fn1 = lambda: math_ops.add(value, 1.0)
fn2 = lambda: math_ops.subtract(value, 1.0)
exit(control_flow_ops.cond(pred, fn1, fn2))
