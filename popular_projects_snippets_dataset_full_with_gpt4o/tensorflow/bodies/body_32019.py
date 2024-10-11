# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
for index, (input_size, filter_size, output_size, stride, padding,
            dilations) in enumerate(CheckGradConfigsToTestExplicit()):
    tf_logging.info(
        "Testing DepthwiseConv2DFilterGradExplicit, %dth config: %r * %r, "
        "stride: %d, padding: %s", index, input_size, filter_size, stride,
        padding)
    # double datatype is currently not supported for convolution ops
    # on the ROCm platform and its support for bfloat16 is unknown.
    data_types = [dtypes.float16, dtypes.float32]
    if not test.is_built_with_rocm():
        data_types.extend([dtypes.float64, dtypes.bfloat16])
    data_formats = ["NHWC", "NCHW"] if test.is_gpu_available() else ["NHWC"]
    for data_type in data_types:
        for data_format in data_formats:
            self._ConstructAndTestGradient(
                input_size,
                filter_size,
                output_size,
                stride,
                padding,
                data_type,
                test_input=False,
                use_gpu=True,
                data_format=data_format,
                dilations=dilations)
