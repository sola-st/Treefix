# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
x1 = np.random.rand(*filter_sizes).astype(np.float32)
x2 = np.random.rand(*output_sizes).astype(np.float32)

def _GetVal(use_xla):
    with self.session():
        t1 = array_ops.placeholder(np.float32, shape=filter_sizes)
        t2 = array_ops.placeholder(np.float32, shape=output_sizes)
        if use_xla:
            with self.test_scope():
                t0 = constant_op.constant(input_sizes, shape=[len(input_sizes)])
                backprop = nn_ops.depthwise_conv2d_native_backprop_input(
                    t0,
                    t1,
                    t2,
                    strides=[1, stride, stride, 1],
                    dilations=[1, dilation, dilation, 1],
                    padding=padding)
        else:
            # TODO(wangtao): figure out gradient with stride > 1.
            # depthwise_conv2d_native_backprop_input on CPU doesn't support
            # dilation.
            t3 = array_ops.space_to_batch(
                t2, block_size=dilation, paddings=[[0, 0], [0, 0]])
            input_sizes_transform = [
                input_sizes[0] * dilation * dilation, input_sizes[1] // dilation,
                input_sizes[2] // dilation, input_sizes[3]
            ]
            t0 = constant_op.constant(
                input_sizes_transform, shape=[len(input_sizes)])
            backprop_naive = nn_ops.depthwise_conv2d_native_backprop_input(
                t0, t1, t3, strides=[1, stride, stride, 1], padding=padding)
            backprop = array_ops.batch_to_space(
                backprop_naive, [[0, 0], [0, 0]], block_size=dilation)

        ret = backprop.eval({t1: x1, t2: x2})
        self.assertShapeEqual(ret, backprop)
        exit(ret)

gpu_value = _GetVal(use_xla=True)
cpu_value = _GetVal(use_xla=False)

# TODO (b/64210055): Tolerance for TPU is high.
self.assertAllClose(cpu_value, gpu_value, rtol=1e-2, atol=1e-3)
