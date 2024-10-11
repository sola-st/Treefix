# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
x1 = np.random.rand(*filter_sizes).astype(np.float32)
x2 = np.random.rand(*output_sizes).astype(np.float32)

def _GetVal(data_format, use_gpu):
    with test_util.device(use_gpu):
        if data_format == "NCHW":
            new_input_sizes = test_util.NHWCToNCHW(input_sizes)
        else:
            new_input_sizes = input_sizes
        t0 = constant_op.constant(new_input_sizes, shape=[len(new_input_sizes)])
        t1 = constant_op.constant(x1, shape=filter_sizes)
        t2 = constant_op.constant(x2, shape=output_sizes)
        strides = [1] + conv_strides + [1]
        if data_format == "NCHW":
            t2 = test_util.NHWCToNCHW(t2)
            strides = test_util.NHWCToNCHW(strides)
        conv = nn_ops.conv2d_backprop_input(
            t0,
            t1,
            t2,
            strides=strides,
            padding=padding,
            data_format=data_format)
        if data_format == "NCHW":
            conv = test_util.NCHWToNHWC(conv)
        ret = self.evaluate(conv)
        self.assertShapeEqual(ret, conv)
        exit(ret)

values = []
for (data_format, use_gpu) in GetTestConfigs():
    values.append(_GetVal(data_format, use_gpu))

for i in range(1, len(values)):
    self.assertAllClose(values[0], values[i], rtol=1e-2, atol=1e-2)
