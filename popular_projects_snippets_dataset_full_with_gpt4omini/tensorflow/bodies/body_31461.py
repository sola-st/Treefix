# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilterExplicitPadding(
        input_sizes=[2, 3, 1, 1],
        filter_sizes=[2, 1, 1, 1],
        output_sizes=[2, 2, 5, 1],
        strides=[3, 1],
        padding=[[2, 2], [2, 2]],
        data_format=data_format,
        use_gpu=use_gpu)

    self._RunAndVerifyBackpropFilterExplicitPadding(
        input_sizes=[1, 3, 6, 1],
        filter_sizes=[3, 2, 1, 1],
        output_sizes=[1, 3, 4, 1],
        strides=[1, 2],
        padding=[[2, 2], [2, 2]],
        data_format=data_format,
        use_gpu=use_gpu,
        dilations=[2, 3])
