# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if test.is_gpu_available(cuda_only=True) or test_util.IsMklEnabled():
    for (data_format, use_gpu) in GetTestConfigs():
        self._RunAndVerifyBackpropFilterDilation(
            input_sizes=[1, 3, 4, 3],
            filter_sizes=[2, 2, 3, 3],
            output_sizes=[1, 1, 2, 3],
            strides=[1, 1],
            dilations=[2, 2],
            padding="VALID",
            data_format=data_format,
            use_gpu=use_gpu,
            err=1e-5)
