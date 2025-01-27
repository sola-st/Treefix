# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if test.is_gpu_available(cuda_only=True) or test_util.IsMklEnabled():
    for (data_format, use_gpu) in GetTestConfigs():
        # The GPU version of this test is not very stable. So adjusting the
        # error threshold to 1e-4.
        self._RunAndVerifyBackpropInputDilation(
            input_sizes=[1, 3, 2, 3],
            filter_sizes=[2, 2, 3, 3],
            output_sizes=[1, 1, 2, 3],
            strides=[1, 1],
            dilations=[2, 1],
            padding="VALID",
            data_format=data_format,
            use_gpu=use_gpu,
            err=1e-4)
