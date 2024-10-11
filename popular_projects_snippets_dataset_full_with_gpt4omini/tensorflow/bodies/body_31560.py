# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
for (data_format, use_gpu) in [("NHWC", False), ("NCHW", False)]:
    np_input = np.arange(1.0, 129.0).reshape([4, 1, 1, 32]).astype(np.float32)
    self._testGradient(np_input,
                       np.random.rand(32).astype(np.float32), dtypes.float32,
                       data_format, use_gpu)
