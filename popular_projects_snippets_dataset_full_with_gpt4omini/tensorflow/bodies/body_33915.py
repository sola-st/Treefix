# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    with ops.device(test.gpu_device_name()):
        a = constant_op.constant(1.0)
        a_handle = self.evaluate(session_ops.get_session_handle(a))
    with ops.device("/cpu:0"):
        b = constant_op.constant(2.0)
        b_handle = self.evaluate(session_ops.get_session_handle(b))

    a_p, a_t = session_ops.get_session_tensor(a_handle.handle, dtypes.float32)
    b_p, b_t = session_ops.get_session_tensor(b_handle.handle, dtypes.float32)
    c = math_ops.add(a_t, b_t)
    c_handle = sess.run(
        session_ops.get_session_handle(c),
        feed_dict={a_p: a_handle.handle,
                   b_p: b_handle.handle})
    self.assertEqual(3.0, c_handle.eval())
