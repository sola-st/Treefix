# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
total_size_tensor = np.prod(tensor_in_sizes)
total_size_filter = np.prod(filter_in_sizes)

# Initializes the input tensor with array containing numbers from 0 to 1.
# We keep the input tensor values fairly small to avoid overflowing float16
# during the conv3d.
x1 = [f * 1.0 / total_size_tensor for f in range(1, total_size_tensor + 1)]
x2 = [f * 1.0 / total_size_filter for f in range(1, total_size_filter + 1)]
with self.cached_session(use_gpu=use_gpu):
    t1 = constant_op.constant(x1, shape=tensor_in_sizes, dtype=dtype)
    t2 = constant_op.constant(x2, shape=filter_in_sizes, dtype=dtype)

    if isinstance(stride, collections_abc.Iterable):
        strides = [1] + list(stride) + [1]
    else:
        strides = [1, stride, stride, stride, 1]

    if data_format == "NCDHW":
        t1 = test_util.NHWCToNCHW(t1)
        strides = test_util.NHWCToNCHW(strides)
    conv = nn_ops.conv3d(t1, t2, strides, padding=padding,
                         data_format=data_format)
    if data_format == "NCDHW":
        conv = test_util.NCHWToNHWC(conv)

    exit(conv)
