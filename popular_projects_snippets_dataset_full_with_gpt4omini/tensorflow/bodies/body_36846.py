# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu):
    x = constant_op.constant(10)
    pred = math_ops.less(1, 2)
    fn1 = lambda: math_ops.add(x, 1)
    fn2 = lambda: math_ops.subtract(x, 1)
    r = control_flow_ops.cond(pred, fn1, fn2)

    result = self.evaluate(r)
self.assertAllEqual(11, result)
