# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
tf_dtype, tol = tf_dtype_tol
np_dtype = tf_dtype.as_numpy_dtype
expected = np_window_fn(window_length,
                        symmetric=not periodic).astype(np_dtype)
actual = tf_window_fn(window_length, periodic=periodic,
                      dtype=tf_dtype)
self.assertAllClose(expected, actual, tol, tol)
