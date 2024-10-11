# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with self.cached_session() as sess:
    i = constant_op.constant(0)
    c = lambda i: math_ops.less(i, 10)
    b = lambda i: math_ops.add(i, 1)
    control_flow_ops.while_loop(
        c, b, [i], maximum_iterations=maximum_iterations)
    for op in sess.graph.get_operations():
        control_flow_context = op._get_control_flow_context()
        if control_flow_context:
            self.assertProtoEquals(
                control_flow_context.to_proto(),
                control_flow_ops.WhileContext.from_proto(
                    control_flow_context.to_proto()).to_proto())
