# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected = [161.0, 182.0, 287.0, 308.0]
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilter(
        input_sizes=[1, 3, 6, 1],
        filter_sizes=[2, 2, 1, 1],
        output_sizes=[1, 2, 3, 1],
        strides=[1, 2],
        padding="VALID",
        expected=expected,
        data_format=data_format,
        use_gpu=use_gpu)
