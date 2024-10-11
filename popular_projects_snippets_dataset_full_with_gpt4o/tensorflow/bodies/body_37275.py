# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():
    pred = math_ops.less(1, 2)
    fn1 = lambda: [constant_op.constant(10)]
    fn2 = lambda: [constant_op.constant(20)]
    r = control_flow_ops.cond(pred, fn1, fn2)

    self.assertAllEqual(r.numpy(), 10)
    self.assertFalse(isinstance(r, list))
