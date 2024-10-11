# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
total_size_tensor = np.prod(tensor_in_sizes)
total_size_filter = np.prod(filter_in_sizes)

# Initializes the input tensor with array containing incrementing
# numbers from 1.
x1 = [f * 1.0 for f in range(1, total_size_tensor + 1)]
x2 = [f * 1.0 for f in range(1, total_size_filter + 1)]
with self.cached_session(use_gpu=use_gpu):
    t1 = constant_op.constant(x1, shape=tensor_in_sizes)
    t2 = constant_op.constant(x2, shape=filter_in_sizes)
    if isinstance(stride, collections_abc.Iterable):
        strides = list(stride)
    else:
        strides = [stride, stride, stride]
    if data_format == "NCDHW":
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
    computed = nn_ops.conv3d(
        t1,
        t2,
        strides=full_strides,
        dilations=full_dilation,
        padding=padding,
        data_format=data_format)
    if data_format == "NCDHW":
        expected = test_util.NCHWToNHWC(expected)
        computed = test_util.NCHWToNHWC(computed)
exit((expected, computed))
