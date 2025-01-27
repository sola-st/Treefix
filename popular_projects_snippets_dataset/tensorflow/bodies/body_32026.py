# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
for index, (input_size, filter_size, output_size, stride, padding,
            dilations) in enumerate(ConfigsToTest()):
    if dilations:
        continue
    tf_logging.info(
        "Testing DepthwiseConv2DFilterGradCompare, %dth config: %r * %r, "
        "stride: %d, padding: %s", index, input_size, filter_size, stride,
        padding)
    self._CompareBackpropFilter(input_size, filter_size, output_size, stride,
                                padding, "float32")
    # Convolutions on the ROCm platform don't support double dtype. And its
    # support for bf16 is unknown. So, we skip these tests.
    if test.is_built_with_rocm():
        continue
    self._CompareBackpropFilter(input_size, filter_size, output_size, stride,
                                padding, "float64")

    self._CompareBackpropFilter(input_size, filter_size, output_size, stride,
                                padding, "bfloat16")
