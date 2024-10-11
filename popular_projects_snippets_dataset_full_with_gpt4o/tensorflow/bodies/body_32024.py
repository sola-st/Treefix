# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
with self.cached_session(use_gpu=use_gpu):
    t0 = constant_op.constant(x0, shape=input_sizes, dtype=dtype)
    t1 = constant_op.constant(filter_sizes, shape=[len(filter_sizes)])
    t2 = constant_op.constant(x2, shape=output_sizes, dtype=dtype)
    strides = [1, stride, stride, 1]
    padding = padding_nhwc
    if data_format == "NCHW":
        t0 = array_ops.transpose(t0, [0, 3, 1, 2])
        t2 = array_ops.transpose(t2, [0, 3, 1, 2])
        strides = [1, 1, stride, stride]
        padding = padding_nchw
    backprop = nn_ops.depthwise_conv2d_native_backprop_filter(
        t0,
        t1,
        t2,
        strides=strides,
        padding=padding,
        data_format=data_format)
    ret = self.evaluate(backprop)
    self.assertShapeEqual(ret, backprop)
    exit(ret)
