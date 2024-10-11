# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32)
    control_flow_ops.cond(
        constant_op.constant(True), lambda: x + 2, lambda: x + 0)
    graph = ops.get_default_graph()
    for op in graph.get_operations():
        for t in op.inputs:
            if graph.is_fetchable(t.op):
                sess.run(t, feed_dict={x: 3})
            else:
                with self.assertRaisesRegex(ValueError,
                                            "has been marked as not fetchable"):
                    sess.run(t, feed_dict={x: 3})
