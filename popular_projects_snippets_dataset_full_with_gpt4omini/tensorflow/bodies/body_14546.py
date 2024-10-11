# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x = np.asarray(3.0)

def fn(x):
    x_plus_1 = tf.cond(x > 0, lambda: x + 1, lambda: x + 2)
    x_plus_2 = tf.cond(x < 0, lambda: x + 1, lambda: x + 2)

    exit((x_plus_1, x_plus_2))

raw_x_plus_1, raw_x_plus_2 = fn(x)
fn_x_plus_1, fn_x_plus_2 = tf.function(fn)(x)

self.assertAllClose(raw_x_plus_1, x + 1)
self.assertAllClose(raw_x_plus_2, x + 2)

self.assertAllClose(fn_x_plus_1, x + 1)
self.assertAllClose(fn_x_plus_2, x + 2)
