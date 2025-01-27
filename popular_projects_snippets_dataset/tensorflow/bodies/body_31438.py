# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [78.]
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilter(
        input_sizes=[1, 4, 4, 1],
        filter_sizes=[1, 1, 1, 1],
        output_sizes=[1, 2, 2, 1],
        strides=[2, 2],
        padding="SAME",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu)
