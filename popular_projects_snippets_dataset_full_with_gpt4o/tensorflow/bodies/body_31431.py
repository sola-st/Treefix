# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
with test_util.device(use_gpu):
    t0 = constant_op.constant(x0, shape=input_sizes)
    t1 = constant_op.constant(filter_sizes, shape=[len(filter_sizes)])
    t2 = constant_op.constant(x2, shape=output_sizes)
    strides = [1] + conv_strides + [1]
    if data_format == "NCHW":
        t0 = test_util.NHWCToNCHW(t0)
        t2 = test_util.NHWCToNCHW(t2)
        strides = test_util.NHWCToNCHW(strides)
    conv = nn_ops.conv2d_backprop_filter(
        t0,
        t1,
        t2,
        strides=strides,
        padding=padding,
        data_format=data_format)
    ret = self.evaluate(conv)
    self.assertShapeEqual(ret, conv)
    exit(ret)
