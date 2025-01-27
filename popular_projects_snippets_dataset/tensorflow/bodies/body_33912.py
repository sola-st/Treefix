# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    # Return a handle.
    a = constant_op.constant(10)
    b = constant_op.constant(5)
    c = math_ops.multiply(a, b)
    h = session_ops.get_session_handle(c)
    h = self.evaluate(h)

    # Feed a tensor handle.
    f, x = session_ops.get_session_tensor(h.handle, dtypes.int32)
    y = math_ops.multiply(x, 10)
    self.assertEqual(500, sess.run(y, feed_dict={f: h.handle}))

    # Feed another tensor handle.
    with ops.device(test.gpu_device_name()):
        a = constant_op.constant(10)
        h = session_ops.get_session_handle(a)
        h = self.evaluate(h)
        self.assertEqual(100, sess.run(y, feed_dict={f: h.handle}))
