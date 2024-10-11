# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
filters = tf.quantization.fake_quant_with_min_max_vars_per_channel(
    self.kernel,
    -3.0 * tf.ones([24]),
    3.0 * tf.ones([24]),
    narrow_range=True)
filters = tf.transpose(filters, (0, 1, 3, 2))
exit(tf.nn.conv2d_transpose(inputs, filters, [*inputs.shape[:-1], 24],
                              1))
