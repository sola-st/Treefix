# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
for index, (input_size, filter_size, _, stride, padding,
            dilations) in enumerate(ConfigsToTestExplicit()):
    tf_logging.info(
        "Testing DepthwiseConv2D, %dth config: %r * %r, stride: %d, padding: "
        "%s", index, input_size, filter_size, stride, padding)
    # double datatype is currently not supported for convolution ops
    # on the ROCm platform and its support for bfloat16 is unknown.
    data_types = [dtypes.float16, dtypes.float32]
    if not test.is_built_with_rocm():
        data_types.extend([dtypes.float64, dtypes.bfloat16])
    data_formats = ["NHWC", "NCHW"] if test.is_gpu_available() else ["NHWC"]
    for data_type in data_types:
        for data_format in data_formats:
            tolerance = 2e-2 if data_type == dtypes.bfloat16 else None
            self._VerifyValues(
                input_size,
                filter_size,
                stride,
                padding,
                data_type,
                use_gpu=True,
                data_format=data_format,
                dilations=dilations,
                tolerance=tolerance)
