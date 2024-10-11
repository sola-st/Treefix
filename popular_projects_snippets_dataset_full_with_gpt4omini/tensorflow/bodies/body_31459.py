# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilterExplicitPadding(
        input_sizes=[1, 2, 3, 1],
        filter_sizes=[2, 2, 1, 1],
        output_sizes=[1, 1, 2, 1],
        strides=[1, 1],
        padding=[[0, 0], [0, 0]],
        data_format=data_format, use_gpu=use_gpu)

    self._RunAndVerifyBackpropFilterExplicitPadding(
        input_sizes=[1, 3, 4, 2],
        filter_sizes=[2, 2, 2, 3],
        output_sizes=[1, 1, 2, 3],
        strides=[2, 2],
        padding=[[0, 0], [0, 0]],
        data_format=data_format, use_gpu=use_gpu)
