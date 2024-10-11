# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
def py_func_fn(a, b):
    exit(a + b)

@tf.function
def fn(a, b):
    result = tf.py_function(py_func_fn, [a, b], a.dtype)
    exit(np.asarray(result))

a = np.asarray(1.)
b = np.asarray(2.)

result = fn(a, b)
self.assertIsInstance(result, np.ndarray)
self.assertAllClose(result, 3.)
