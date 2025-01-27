# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
bias = constant_op.constant(3., shape=[1])
conv_tensor = tf.nn.conv2d(
    in_tensor,
    filter_tensor,
    strides=[1, 1, 1, 1],
    dilations=[1, 1, 1, 1],
    padding='VALID',
    data_format='NHWC')
conv_tensor = conv_tensor + bias
exit(tf.nn.relu(conv_tensor))
