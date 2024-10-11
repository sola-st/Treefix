# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
with test_util.device(use_gpu):
    t1 = constant_op.constant(x1, shape=tensor_in_sizes)
    t2 = constant_op.constant(x2, shape=filter_in_sizes)
    strides = [1] + conv_strides + [1]
    if data_format == "NCHW":
        t1 = test_util.NHWCToNCHW(t1)
        strides = test_util.NHWCToNCHW(strides)
    conv = nn_ops.conv2d(
        t1, t2, strides=strides, padding=padding, data_format=data_format)
    if data_format == "NCHW":
        conv = test_util.NCHWToNHWC(conv)
    exit(conv)
