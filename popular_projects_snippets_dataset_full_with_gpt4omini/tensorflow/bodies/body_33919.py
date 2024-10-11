# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    a = constant_op.constant(10.0)
    b = constant_op.constant(5.0)
    c = math_ops.multiply(a, b)
    h_c = self.evaluate(session_ops.get_session_handle(c))
    d = array_ops.identity(c)

    c_val = sess.run(c, feed_dict={c: h_c})
    self.assertAllClose(50.0, c_val)

    d_val = sess.run(d, feed_dict={c: h_c})
    self.assertAllClose(50.0, d_val)

    c_val, d_val = sess.run([c, d], feed_dict={c: h_c, d: 60.0})
    self.assertAllClose(50.0, c_val)
    self.assertAllClose(60.0, d_val)

    c_val, d_val = sess.run([c, d], feed_dict={c: 60.0, d: h_c})
    self.assertAllClose(60.0, c_val)
    self.assertAllClose(50.0, d_val)

    c_val, d_val = sess.run([c, d], feed_dict={c: h_c, d: h_c})
    self.assertAllClose(50.0, c_val)
    self.assertAllClose(50.0, d_val)
