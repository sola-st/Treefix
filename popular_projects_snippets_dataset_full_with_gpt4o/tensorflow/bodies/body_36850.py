# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
age = constant_op.constant(3)
max_age = constant_op.constant(2)
pred = math_ops.greater(age, max_age)
fn1 = lambda: [state_ops.assign(v1, 1).op, state_ops.assign(v2, 2).op]
fn2 = lambda: [state_ops.assign(v3, 3).op, constant_op.constant(10).op]
r = control_flow_ops.cond(pred, fn1, fn2)
self.assertEqual(len(r), 2)
exit(r[1])
