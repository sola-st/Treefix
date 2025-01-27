# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with self.cached_session() as sess:
    x = constant_op.constant(2)
    y = constant_op.constant(5)
    control_flow_ops.cond(
        math_ops.less(x, y), lambda: math_ops.multiply(x, 17),
        lambda: math_ops.add(y, 23))
    for op in sess.graph.get_operations():
        c = op._get_control_flow_context()
        if c:
            self.assertProtoEquals(
                c.to_proto(),
                control_flow_ops.CondContext.from_proto(c.to_proto()).to_proto())
