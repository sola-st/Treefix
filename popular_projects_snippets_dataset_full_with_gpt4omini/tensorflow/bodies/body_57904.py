# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
filters = tf.quantization.fake_quant_with_min_max_vars(
    self.kernel, -3.0, 3.0, narrow_range=True)
filters = tf.transpose(filters, (0, 1, 3, 2))
result = tf.nn.conv2d_transpose(inputs, filters,
                                [*inputs.shape[:-1], 3], 1)
result = tf.nn.bias_add(result, self.bias)
result = tf.nn.relu(result)

exit(tf.quantization.fake_quant_with_min_max_vars(
    result, -3.0, 3.0, narrow_range=True))
