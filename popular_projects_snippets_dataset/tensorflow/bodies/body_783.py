# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
for index, (input_size, filter_size, _, stride,
            padding) in enumerate(ConfigsToTest()):
    print("Testing DepthwiseConv2D,", index, "th config:", input_size, "*",
          filter_size, "stride:", stride, "padding:", padding)
    for data_type in self.float_types:
        # TODO(phawkins): the reference implementation only supports float32.
        if data_type == np.float32:
            self._VerifyValues(
                input_size, filter_size, stride, padding, data_type)
