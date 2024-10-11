# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
x1 = self._CreateNumpyTensor(tensor_in_sizes)
x2 = self._CreateNumpyTensor(filter_in_sizes)
with test_util.device(use_gpu):
    t1 = constant_op.constant(x1, shape=tensor_in_sizes)
    t2 = constant_op.constant(x2, shape=filter_in_sizes)
    if isinstance(stride, collections_abc.Iterable):
        strides = list(stride)
    else:
        strides = [stride, stride]
    if data_format == "NCHW":
        t1 = test_util.NHWCToNCHW(t1)
        full_strides = [1, 1] + strides
        full_dilation = [1, 1] + dilation
    else:
        full_strides = [1] + strides + [1]
        full_dilation = [1] + dilation + [1]
    expected = nn_ops.convolution(
        t1,
        t2,
        padding=padding,
        strides=strides,
        dilation_rate=dilation,
        data_format=data_format)
    computed = nn_ops.conv2d(
        t1,
        t2,
        strides=full_strides,
        dilations=full_dilation,
        padding=padding,
        data_format=data_format)
    if data_format == "NCHW":
        expected = test_util.NCHWToNHWC(expected)
        computed = test_util.NCHWToNHWC(computed)
exit((expected, computed))
