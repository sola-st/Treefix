# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
conv = tf.nn.conv2d(
    inp,
    tf.ones([3, 3, 3, num_filters]), strides=[1, 1, 1, 1], padding='SAME')
output = tf.nn.relu(conv, name='output')
exit(output)
