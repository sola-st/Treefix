# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
x1 = self._CreateNumpyTensor(input_sizes)
x2 = self._CreateNumpyTensor(filter_sizes)
default_dilations = (dilations[0] == 1 and dilations[1] == 1)
if default_dilations or use_gpu:
    with self.cached_session(use_gpu=use_gpu):
        if data_format == "NCHW":
            input_sizes = test_util.NHWCToNCHW(input_sizes)
        t1 = constant_op.constant(x1, shape=input_sizes)
        t2 = constant_op.constant(x2, shape=filter_sizes)
        full_strides = [1] + strides + [1]
        full_dilations = [1] + dilations + [1]
        if data_format == "NCHW":
            full_strides = test_util.NHWCToNCHW(full_strides)
            full_dilations = test_util.NHWCToNCHW(full_dilations)
        conv_forward = nn_ops.conv2d(
            t1,
            t2,
            strides=full_strides,
            dilations=full_dilations,
            padding=padding,
            data_format=data_format)
        conv_forward_2 = nn_ops.convolution(
            t1,
            t2,
            padding=padding,
            strides=strides,
            dilation_rate=dilations,
            data_format=data_format)
        if data_format == "NCHW":
            conv_forward = test_util.NCHWToNHWC(conv_forward)
            conv_forward_2 = test_util.NCHWToNHWC(conv_forward_2)
        conv = gradients_impl.gradients(conv_forward, t2)[0]
        conv_2 = gradients_impl.gradients(conv_forward, t2)[0]
        value = self.evaluate(conv)
        value_2 = self.evaluate(conv_2)
        self.assertShapeEqual(value, conv)
        self.assertShapeEqual(value_2, conv_2)
    tf_logging.debug("expected = %s", value_2)
    tf_logging.debug("actual = %s", value)
    self.assertArrayNear(value_2.flatten(), value.flatten(), err)
