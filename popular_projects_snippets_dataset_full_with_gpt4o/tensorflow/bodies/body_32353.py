# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""Check that kaiser_window matches np.kaiser behavior."""
self.assertAllClose(
    np.kaiser(window_length, beta),
    window_ops.kaiser_window(window_length, beta, tf_dtype_tol[0]),
    tf_dtype_tol[1], tf_dtype_tol[1])
