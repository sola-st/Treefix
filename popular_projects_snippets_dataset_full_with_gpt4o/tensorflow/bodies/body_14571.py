# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x = np.asarray(3.0)
y = np.asarray(2.0)

add = lambda x, y: x + y
add_fn = tf.function(add)

raw_result = add(x, y)
fn_result = add_fn(x, y)

self.assertIsInstance(raw_result, np.ndarray)
self.assertIsInstance(fn_result, np.ndarray)
self.assertAllClose(raw_result, fn_result)
