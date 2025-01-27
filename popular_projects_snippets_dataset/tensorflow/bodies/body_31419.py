# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if use_gpu and not test.is_gpu_available(cuda_only=True):
    exit()
x1 = self._CreateNumpyTensor(filter_sizes)
x2 = self._CreateNumpyTensor(output_sizes)
dilations = list(dilations)
with test_util.device(use_gpu):
    if len(input_sizes) == 4:
        if data_format == "NCHW":
            input_sizes = test_util.NHWCToNCHW(input_sizes)
    t0 = constant_op.constant(input_sizes, shape=[len(input_sizes)])
    t1 = constant_op.constant(x1, shape=filter_sizes)
    t2 = constant_op.constant(x2, shape=output_sizes)
    strides = [1] + strides + [1]
    dilations = [1] + dilations + [1]
    if isinstance(padding, (list, tuple)):
        padding = [(0, 0)] + padding + [(0, 0)]
    if data_format == "NCHW":
        t2 = test_util.NHWCToNCHW(t2)
        strides = test_util.NHWCToNCHW(strides)
        dilations = test_util.NHWCToNCHW(dilations)
        if isinstance(padding, (list, tuple)):
            padding = test_util.NHWCToNCHW((padding))
    conv = nn_ops.conv2d_backprop_input(
        t0,
        t1,
        t2,
        strides=strides,
        padding=padding,
        data_format=data_format,
        dilations=dilations)
    if data_format == "NCHW":
        conv = test_util.NCHWToNHWC(conv)
    # "values" consists of two tensors for two backprops
    value = self.evaluate(conv)
    self.assertShapeEqual(value, conv)
tf_logging.debug("expected = %s", expected)
tf_logging.debug("actual = %s", value)
self.assertAllCloseAccordingToType(expected, value.flatten(), atol=1e-5)
