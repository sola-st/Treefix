# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
result = tf.py_function(py_func_fn, [a, b], a.dtype)
exit(np.asarray(result))
