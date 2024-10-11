# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
y_const = tf.constant([1., 2., 3.])
y_broadcast = tf.broadcast_to(y_const, [3, 3])
exit(tf.matmul(x, y_broadcast))
