# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
tanh = tf.math.tanh(inp)
# Flex delegate will merge the consecutive conv3d and erf ops into one
# Delegate node.
conv3d = tf.nn.conv3d(
    tanh,
    tf.ones([3, 3, 3, 3, 3]),
    strides=[1, 1, 1, 1, 1],
    padding='SAME')
erf = tf.math.erf(conv3d)
output = tf.math.tanh(erf)
exit(output)
