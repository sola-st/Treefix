# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
for data_format, use_gpu in GetTestConfigs():
    self._VerifyOneTest(pool_func, input_sizes, window, strides, padding,
                        data_format, dtypes.float32, expected, use_gpu)
    # Don't test bfloat16 on GPU if there is no GPU available.
    if (not use_gpu) or test_util.is_gpu_available(cuda_only=True):
        self._VerifyOneTest(pool_func, input_sizes, window, strides, padding,
                            data_format, dtypes.bfloat16, expected, use_gpu)
