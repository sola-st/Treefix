# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
for (data_format, use_gpu) in [("NHWC", False), ("NHWC", True),
                               ("NCHW", False), ("NCHW", True)]:
    for dtype in (dtypes.float16, dtypes.float32, dtypes.float64,
                  dtypes.bfloat16):
        # pylint: disable=too-many-function-args
        np_input = np.array(
            [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            dtype=dtype.as_numpy_dtype).reshape(1, 3, 2)
        bias = np.array([1.3, 2.4], dtype=dtype.as_numpy_dtype)
        self._testGradient(np_input, bias, dtype, data_format, use_gpu)
