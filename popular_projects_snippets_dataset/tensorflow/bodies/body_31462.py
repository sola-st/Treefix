# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilterExplicitPadding(
        input_sizes=[1, 2, 3, 1],
        filter_sizes=[2, 2, 1, 1],
        output_sizes=[1, 10, 8, 1],
        strides=[1, 1],
        padding=[[1, 8], [4, 2]],
        data_format=data_format,
        use_gpu=use_gpu,
        err=1e-4)

    self._RunAndVerifyBackpropFilterExplicitPadding(
        input_sizes=[1, 5, 3, 1],
        filter_sizes=[3, 2, 1, 1],
        output_sizes=[1, 4, 8, 1],
        strides=[3, 1],
        padding=[[1, 8], [4, 2]],
        use_gpu=use_gpu,
        data_format=data_format)
