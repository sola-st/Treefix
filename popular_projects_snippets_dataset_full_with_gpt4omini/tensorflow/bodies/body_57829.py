# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# ceil kernel does not support int8 nor int16 types neither.
left = tf.math.ceil(a)
right = tf.nn.tanh(b)
add = tf.math.add(left, right)
# ceil kernel does not support int8 nor int16 types neither.
output = tf.math.ceil(add)
exit((output, right))
