# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
p = array_ops.placeholder(dtypes.bool, shape=[])
v = constant_op.constant(10)
fn1 = lambda: math_ops.add(v, 1)
fn2 = lambda: math_ops.subtract(v, 1)
y = control_flow_ops.cond(p, fn1, fn2)
grad = gradients_impl.gradients(y, [v])
self.assertAllEqual([None], grad)
