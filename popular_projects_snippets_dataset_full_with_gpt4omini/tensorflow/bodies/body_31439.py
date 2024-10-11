# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [1.0, 2.0, 2.0, 4.0, 3.0, 6.0, 4.0, 8.0]
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilter(
        input_sizes=[1, 2, 2, 1],
        filter_sizes=[2, 2, 1, 2],
        output_sizes=[1, 1, 1, 2],
        strides=[1, 1],
        padding="VALID",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu)
