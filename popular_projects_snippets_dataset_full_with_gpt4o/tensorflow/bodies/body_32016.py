# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
for index, (input_size, filter_size, output_size, stride, padding,
            dilations) in enumerate(CheckGradConfigsToTest()):
    # The CuDNN depthwise conv (filter gradient) is turned on only when
    # input/output is float16(half). See cudnn release note 7.6.3.
    tf_logging.info(
        "Testing DepthwiseConv2DFilterGradCudnn, %dth config: %r * %r, "
        "stride: %d, padding: %s", index, input_size, filter_size, stride,
        padding)
    data_types = [dtypes.float16, dtypes.bfloat16]
    for data_type in data_types:
        self._ConstructAndTestGradient(
            input_size,
            filter_size,
            output_size,
            stride,
            padding,
            data_type,
            test_input=False,
            use_gpu=True,
            data_format="NCHW",
            dilations=dilations)
        self._ConstructAndTestGradient(
            input_size,
            filter_size,
            output_size,
            stride,
            padding,
            data_type,
            test_input=False,
            use_gpu=True,
            data_format="NHWC",
            dilations=dilations)
