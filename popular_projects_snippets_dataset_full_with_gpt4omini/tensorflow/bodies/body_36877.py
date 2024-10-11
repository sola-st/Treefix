# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = constant_op.constant(10)
    y = constant_op.constant(200)
    pred = math_ops.less(1, 2)
    fn1 = lambda: {"a": math_ops.add(x, y), "b": math_ops.add(x, y)}
    fn2 = lambda: {"a": y, "b": y}
    r = control_flow_ops.cond(pred, fn1, fn2)
    test_result = self.evaluate(r)
    self.assertDictEqual({"a": 210, "b": 210}, test_result)
