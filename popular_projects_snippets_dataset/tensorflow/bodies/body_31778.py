# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
for seed in range(5):
    p = self._genParams(use_cudnn, data_format, dtype, seed=seed)
    input_data, filter_data, strides, padding, _ = p

    result_a = nn_impl.depthwise_conv2d_v2(input_data, filter_data, strides,
                                           padding, data_format)
    result_b = nn_impl.depthwise_conv2d_v2(input_data, filter_data, strides,
                                           padding, data_format)

    self.assertAllEqual(result_a, result_b)
