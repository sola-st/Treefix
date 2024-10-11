# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    a = variables.Variable(12.0)
    inc_a = state_ops.assign_add(a, 2.0)
    b = math_ops.add(a, 5.0)
    self.evaluate(a.initializer)

    h_a_read = sess.run(session_ops.get_session_handle(a.read_value()))
    self.assertAllClose(12.0, self.evaluate(a))

    self.assertAllClose(17.0, sess.run(b, feed_dict={a: h_a_read}))
    self.evaluate(inc_a)
    self.assertAllClose(19.0, sess.run(b, feed_dict={a: h_a_read}))
