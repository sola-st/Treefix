# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant(10)
y = constant_op.constant(200)
pred = math_ops.less(1, 2)
fn1 = lambda: [[math_ops.add(x, y), math_ops.add(x, y)]]
fn2 = lambda: [[y, y]]
# Pass strict=True flag as cond_v2 allows for tensors to be
# in nested output structures as singletons
r = control_flow_ops.cond(pred, fn1, fn2, strict=True)
test_result = self.evaluate(r)
self.assertListEqual([[210, 210]], test_result)
