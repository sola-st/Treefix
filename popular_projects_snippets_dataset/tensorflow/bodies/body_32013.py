# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
for index, (input_size, filter_size, output_size, stride, padding,
            dilations) in enumerate(CheckGradConfigsToTest()):
    tf_logging.info(
        "Testing DepthwiseConv2DInputGrad, %dth config: %r * %r, stride: %d, "
        "padding: %s", index, input_size, filter_size, stride, padding)
    # double datatype is currently not supported for convolution ops
    # on the ROCm platform
    optional_float64 = [] if test.is_built_with_rocm() else [dtypes.float64]
    for data_type in ([dtypes.float32] + optional_float64):
        self._ConstructAndTestGradient(
            input_size,
            filter_size,
            output_size,
            stride,
            padding,
            data_type,
            test_input=True,
            use_gpu=True,
            dilations=dilations)
        self._ConstructAndTestGradient(
            input_size,
            filter_size,
            output_size,
            stride,
            padding,
            data_type,
            test_input=True,
            use_gpu=True,
            grouped_conv=True,
            dilations=dilations)
