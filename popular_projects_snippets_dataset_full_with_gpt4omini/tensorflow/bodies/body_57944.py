# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
shape = tf.shape(in_tensor)
fill = tf.transpose(tf.fill(shape, 1.))
exit(tf.matmul(fill, in_tensor))
