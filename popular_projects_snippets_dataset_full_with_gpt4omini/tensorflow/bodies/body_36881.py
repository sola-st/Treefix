# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = constant_op.constant(10)
    y = constant_op.constant(200)
    pred = math_ops.less(1, 2)
    fn1 = lambda: {"a": math_ops.add(x, y), "b": math_ops.add(x, y)}
    fn2 = lambda: {"c": y, "d": y}
    v1_msg = "The two structures don't have the same nested structure"
    v2_msg = ("true_fn and false_fn arguments to tf.cond must have the same "
              "number, type, and overall structure of return values.")
    with self.assertRaisesRegex(
        TypeError if control_flow_util.ENABLE_CONTROL_FLOW_V2 else ValueError,
        v2_msg if control_flow_util.ENABLE_CONTROL_FLOW_V2 else v1_msg):
        control_flow_ops.cond(pred, fn1, fn2)
