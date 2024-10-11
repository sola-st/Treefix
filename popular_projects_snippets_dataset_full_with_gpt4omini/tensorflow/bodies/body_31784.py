# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
if tf_config.list_physical_devices("GPU"):
    self.skipTest("Test only runs when there is no GPU")
data_format = "NHWC"  # CPU does not implement NCHW version of op
for dtype in [dtypes.bfloat16.as_numpy_dtype, dtypes.float32,
              dtypes.float64]:
    self._testBackwardDeterminismCase(data_format=data_format, dtype=dtype)
