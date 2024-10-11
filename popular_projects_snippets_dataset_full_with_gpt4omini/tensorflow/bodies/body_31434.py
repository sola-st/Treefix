# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected = []
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilter(
        input_sizes=[1, 2, 3, 1],
        filter_sizes=[2, 2, 1, 0],
        output_sizes=[1, 1, 2, 0],
        strides=[1, 1],
        padding="VALID",
        expected=expected,
        data_format=data_format,
        use_gpu=use_gpu)
