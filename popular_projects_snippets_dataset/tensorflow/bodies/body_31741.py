# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
"""Runs _ConstructAndTestGradientForConfig for all tests configurations."""

for data_format, use_gpu in GetTestConfigs():
    self._ConstructAndTestGradientForConfig(
        pool_func,
        data_format=data_format,
        data_type=dtypes.float32,
        use_gpu=use_gpu,
        **kwargs)
    if use_gpu and test_util.is_gpu_available(cuda_only=True):
        self._ConstructAndTestGradientForConfig(
            pool_func,
            data_format=data_format,
            data_type=dtypes.bfloat16,
            use_gpu=use_gpu,
            **kwargs)
