# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
tanh = tf.math.tanh(inp)
conv3d = tf.nn.conv3d(
    tanh,
    tf.ones([3, 3, 3, 3, 3]),
    strides=[1, 1, 1, 1, 1],
    padding="SAME")
erf = tf.math.erf(conv3d)
output = tf.math.tanh(erf)
exit(output)
