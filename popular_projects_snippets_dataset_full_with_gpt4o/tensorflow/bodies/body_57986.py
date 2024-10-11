# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
y = tf.add(x, x, name='y')
z = tf.add(y, y, name='z')
w = tf.add(z, z, name='w')
exit(w)
