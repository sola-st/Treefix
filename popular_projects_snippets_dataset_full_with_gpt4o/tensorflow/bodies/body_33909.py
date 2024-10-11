# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    # Return a handle and a value
    a = constant_op.constant(10)
    b = constant_op.constant(5)
    p = math_ops.less(a, b)
    c = math_ops.multiply(a, b)
    h = session_ops.get_session_handle(c)
    p, h = self.evaluate([p, h])

    # Run by feeding a tensor handle.
    f, x = session_ops.get_session_tensor(h.handle, dtypes.int32)
    if p:
        y = math_ops.multiply(x, 10)
    else:
        y = math_ops.multiply(x, 100)
    result = sess.run(y, feed_dict={f: h.handle})

    self.assertEqual(5000, result)
