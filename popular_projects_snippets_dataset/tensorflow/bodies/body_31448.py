# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if test.is_gpu_available(cuda_only=True) or test_util.IsMklEnabled():
    for (data_format, use_gpu) in GetTestConfigs():
        self._RunAndVerifyBackpropInputDilation(
            input_sizes=[1, 2, 3, 1],
            filter_sizes=[2, 2, 1, 1],
            output_sizes=[1, 1, 2, 1],
            strides=[1, 1],
            dilations=[1, 2],
            padding="VALID",
            data_format=data_format,
            use_gpu=use_gpu,
            err=1e-5)
