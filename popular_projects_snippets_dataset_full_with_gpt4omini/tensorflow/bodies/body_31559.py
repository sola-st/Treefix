# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
for (data_format, use_gpu) in [("NHWC", False), ("NHWC", True),
                               ("NCHW", False), ("NCHW", True)]:
    for dtype in (dtypes.float16, dtypes.float32, dtypes.float64,
                  dtypes.bfloat16):
        np_input = np.arange(
            1.0, 49.0,
            dtype=dtype.as_numpy_dtype).reshape([1, 2, 3, 4,
                                                 2]).astype(np.float32)
        bias = np.array([1.3, 2.4], dtype=dtype.as_numpy_dtype)
        self._testGradient(np_input, bias, dtype, data_format, use_gpu)
