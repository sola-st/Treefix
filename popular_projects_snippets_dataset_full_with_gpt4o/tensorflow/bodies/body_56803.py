# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_bias_activation.py
bias_input = create_tensor_data(np.float32, (filter_shape[-1],))
out = tf.nn.bias_add(data_input, bias_input, data_format="NHWC")
exit(out)
