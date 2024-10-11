# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    # Return a handle.
    a = constant_op.constant(10)
    b = constant_op.constant(5)
    c = math_ops.multiply(a, b)
    h = session_ops.get_session_handle(c)
    h = self.evaluate(h)

    # Delete using a raw tensor handle.
    raw_h = h.get_raw_handle()
    f, x = session_ops.delete_session_tensor(raw_h)
    sess.run(x, feed_dict={f: raw_h})
