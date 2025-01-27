# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
for index, (input_size, filter_size, output_size, stride,
            padding) in enumerate(ConfigsToTest()):
    print("Testing DepthwiseConv2DFilterGradFormatNCHWCompare,", index,
          "th config:", input_size, "*", filter_size, "producing output",
          output_size, "stride:", stride, "padding:", padding)
    self._CompareBackpropFilter(
        input_size,
        filter_size,
        output_size,
        stride,
        padding,
        data_format="NCHW")
