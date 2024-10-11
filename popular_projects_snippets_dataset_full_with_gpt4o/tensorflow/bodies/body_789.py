# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
for index, (input_size, filter_size, _, stride, dilation,
            padding) in enumerate(ConfigsWithDilationsToTest()):
    print("Testing DilationDepthwiseConv2DFormat,", index, "th config:",
          input_size, "*", filter_size, "stride:", stride, "dilation:",
          dilation, "padding:", padding)
    for data_type in self.float_types:
        # TODO(phawkins): the reference implementation only supports float32.
        if data_type == np.float32:
            self._VerifyValuesWithDilation(
                input_size,
                filter_size,
                stride,
                dilation,
                padding,
                data_type,
                data_format="NCHW")
