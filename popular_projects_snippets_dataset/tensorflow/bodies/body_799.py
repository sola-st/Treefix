# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
for index, (input_size, filter_size, output_size, stride, dilation,
            padding) in enumerate(ConfigsWithDilationsToTest()):
    print("Testing DilationDepthwiseConv2DInputGradWithDilationCompare,",
          index, "th config:", input_size, "*", filter_size, "stride:",
          stride, "dilation:", dilation, "padding:", padding)
    # TODO(wangtao): implement CPU grad computation with stride > 1.
    if stride == 1:
        self._CompareBackpropInputWithDilation(input_size, filter_size,
                                               output_size, stride, dilation,
                                               padding)
