# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    a = constant_op.constant(10.0)
    b = constant_op.constant(5.0)
    c = math_ops.multiply(a, b)
    d = math_ops.multiply(c, c)

    h_c = self.evaluate(session_ops.get_session_handle(c))

    self.assertAllClose(2500.0, sess.run(d, feed_dict={c: h_c}))
