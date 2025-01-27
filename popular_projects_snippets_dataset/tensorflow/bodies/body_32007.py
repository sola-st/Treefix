# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
if not test.is_gpu_available():
    exit()

for index, (input_size, filter_size, _, stride, padding,
            dilations) in enumerate(ConfigsToTest()):
    tf_logging.info(
        "Testing DepthwiseConv2DFormat, %dth config: %r * %r, stride: %d, "
        "padding: %s", index, input_size, filter_size, stride, padding)
    # double datatype is currently not supported for convolution ops
    # on the ROCm platform
    optional_float64 = [] if test.is_built_with_rocm() else [dtypes.float64]
    for data_type in ([dtypes.float32] + optional_float64):
        tolerance = 1e-4 if data_type == dtypes.float32 else 1e-12
        self._VerifyValues(
            input_size,
            filter_size,
            stride,
            padding,
            data_type,
            use_gpu=True,
            data_format="NCHW",
            dilations=dilations,
            tolerance=tolerance)
