# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    value = constant_op.constant(37.0)
    predicate = constant_op.constant(True)
    cond_output = control_flow_ops.cond(
        predicate, lambda: constant_op.constant(0.0), lambda: value)
    result = array_ops.identity(cond_output)
    self.assertEqual(37.0, sess.run(result, feed_dict={predicate: False}))
    self.assertEqual(0.0, sess.run(result, feed_dict={predicate: True}))
    self.assertEqual(0.0, sess.run(result))
