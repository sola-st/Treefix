# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    # Initialize a handle.
    a = constant_op.constant(0)
    h = session_ops.get_session_handle(a)
    h = self.evaluate(h)

    # Do some computation.
    f, x = session_ops.get_session_tensor(h.handle, dtypes.int32)
    b = constant_op.constant(100)
    p = math_ops.less(x, b)
    # Must define the loop body outside the loop.
    h_x = session_ops.get_session_handle(math_ops.add(x, 1))
    while True:
        rp, h = sess.run([p, h_x], feed_dict={f: h.handle})
        if not rp:
            break

    self.assertEqual(101, h.eval())
