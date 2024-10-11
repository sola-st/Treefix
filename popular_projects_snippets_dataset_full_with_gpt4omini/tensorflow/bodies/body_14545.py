# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x_plus_1 = tf.cond(x > 0, lambda: x + 1, lambda: x + 2)
x_plus_2 = tf.cond(x < 0, lambda: x + 1, lambda: x + 2)

exit((x_plus_1, x_plus_2))
