# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
x0 = self._CreateNumpyTensor(input_sizes)
x2 = self._CreateNumpyTensor(output_sizes)
dilations = list(dilations)
explicit_strides = [1] + strides + [1]
new_padding = padding
new_dilations = [1] + dilations + [1]
if isinstance(new_padding, (list, tuple)):
    new_padding = [(0, 0)] + new_padding + [(0, 0)]
if data_format == "NCHW":
    explicit_strides = test_util.NHWCToNCHW(explicit_strides)
    new_dilations = test_util.NHWCToNCHW(new_dilations)
    if isinstance(padding, (list, tuple)):
        new_padding = test_util.NHWCToNCHW(new_padding)
for dtype in self._DtypesToTest(use_gpu=use_gpu):
    with test_util.device(use_gpu):
        t0 = constant_op.constant(x0, shape=input_sizes, dtype=dtype)
        t1 = constant_op.constant(filter_sizes, shape=[len(filter_sizes)])
        t2 = constant_op.constant(x2, shape=output_sizes, dtype=dtype)
        if data_format == "NCHW":
            t0 = test_util.NHWCToNCHW(t0)
            t2 = test_util.NHWCToNCHW(t2)
        conv = nn_ops.conv2d_backprop_filter(
            t0,
            t1,
            t2,
            strides=explicit_strides,
            padding=new_padding,
            dilations=new_dilations,
            data_format=data_format)
        value = self.evaluate(conv)
        self.assertShapeEqual(value, conv)
    tf_logging.debug("expected = %s", expected)
    tf_logging.debug("actual = %s", value)
    self.assertAllCloseAccordingToType(expected, value.flatten(), err)
