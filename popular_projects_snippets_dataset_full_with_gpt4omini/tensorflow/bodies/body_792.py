# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
for index, (input_size, filter_size, output_size, stride,
            padding) in enumerate(ConfigsToTest()):
    print("Testing DepthwiseConv2DInputGradCompare,", index, "th config:",
          input_size, "*", filter_size, "stride:", stride, "padding:",
          padding)
    self._CompareBackpropInput(input_size, filter_size, output_size, stride,
                               padding)
