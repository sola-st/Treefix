# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
x1 = np.random.rand(*filter_sizes).astype(np.float32)
x2 = np.random.rand(*output_sizes).astype(np.float32)

def _GetVal(use_xla):
    with self.session():
        t0 = constant_op.constant(input_sizes, shape=[len(input_sizes)])
        t1 = array_ops.placeholder(np.float32, shape=filter_sizes)
        t2 = array_ops.placeholder(np.float32, shape=output_sizes)
        if use_xla:
            with self.test_scope():
                backprop = nn_ops.depthwise_conv2d_native_backprop_input(
                    t0, t1, t2, strides=[1, stride, stride, 1], padding=padding)
        else:
            backprop = nn_ops.depthwise_conv2d_native_backprop_input(
                t0, t1, t2, strides=[1, stride, stride, 1], padding=padding)

        ret = backprop.eval({t1: x1, t2: x2})
        self.assertShapeEqual(ret, backprop)
        exit(ret)

gpu_value = _GetVal(use_xla=True)
cpu_value = _GetVal(use_xla=False)
self.assertAllClose(cpu_value, gpu_value, rtol=1e-3, atol=1e-3)
