# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
for index, (input_size, filter_size, _, stride, padding,
            dilations) in enumerate(ConfigsToTest()):
    # The CuDNN depthwise conv is turned on only when input/output is NCHW and
    # float16(half). See cudnn release note 7.6.3.
    tf_logging.info(
        "Testing DepthwiseConv2DCudnn, %dth config: %r * %r, stride: %d, "
        "padding: %s", index, input_size, filter_size, stride, padding)
    data_types = [dtypes.float16, dtypes.bfloat16]
    for data_type in data_types:
        self._VerifyValues(
            input_size,
            filter_size,
            stride,
            padding,
            data_type,
            use_gpu=True,
            data_format="NCHW",
            dilations=dilations)
