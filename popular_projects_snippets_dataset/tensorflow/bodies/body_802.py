# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
for index, (input_size, filter_size, output_size, stride, dilation,
            padding) in enumerate(ConfigsWithDilationsToTest()):
    print("Testing DilationDepthwiseConv2DFilterGradCompare,", index,
          "th config:", input_size, "*", filter_size, "producing output",
          output_size, "stride:", stride, "dilation:", dilation, "padding:",
          padding)
    if stride == 1:
        # TODO(wangtao): implement CPU grad computation with stride > 1.
        self._CompareBackpropFilterWithDilation(input_size, filter_size,
                                                output_size, stride, dilation,
                                                padding)
