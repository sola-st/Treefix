# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    c = constant_op.constant(2)
    i0 = constant_op.constant(0)
    r = control_flow_ops.while_loop(lambda i: i < 1000,
                                    lambda i: math_ops.square(c) + i, [i0])
    self.assertEqual(1000, r.eval(feed_dict={i0: 0}))
    feedable_tensors = all_feedables()
    for t in feedable_tensors:
        sess.run(r, feed_dict={t: 3})
    graph = ops.get_default_graph()
    for op in graph.get_operations():
        for t in op.inputs:
            if t not in feedable_tensors and t.dtype is dtypes.int32:
                with self.assertRaisesRegex(ValueError, "may not be fed"):
                    sess.run(r, feed_dict={t: 3})
