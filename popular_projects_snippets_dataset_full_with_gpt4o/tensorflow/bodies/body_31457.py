# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropInputExplicitPadding(
        input_sizes=[1, 3, 3, 1],
        filter_sizes=[2, 1, 1, 1],
        output_sizes=[1, 7, 7, 1],
        strides=[1, 1],
        padding=[[5, 0], [2, 2]],
        data_format=data_format,
        err=5e-5,
        use_gpu=use_gpu)

    self._RunAndVerifyBackpropInputExplicitPadding(
        input_sizes=[1, 4, 2, 1],
        filter_sizes=[3, 3, 1, 1],
        output_sizes=[1, 5, 2, 1],
        strides=[1, 2],
        padding=[[5, 0], [2, 2]],
        data_format=data_format,
        dilations=[2, 1],
        use_gpu=use_gpu)
