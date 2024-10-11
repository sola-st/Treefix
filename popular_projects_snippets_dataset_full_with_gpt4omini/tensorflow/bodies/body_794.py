# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
x0 = np.random.rand(*input_sizes).astype(np.float32)
x2 = np.random.rand(*output_sizes).astype(np.float32)

def _GetVal(use_xla):
    with self.session():
        t0 = array_ops.placeholder(np.float32, shape=input_sizes)
        t1 = constant_op.constant(filter_sizes, shape=[len(filter_sizes)])
        t2 = array_ops.placeholder(np.float32, shape=output_sizes)
        native_t0 = t0
        native_t2 = t2
        strides = [1, stride, stride, 1]

        if use_xla:
            if data_format == "NCHW":
                # Transpose from NWHC input to NCHW
                # Ex. [4, 5, 5, 48] to [4, 48, 5, 5]
                native_t0 = array_ops.transpose(t0, [0, 3, 1, 2])
                native_t2 = array_ops.transpose(t2, [0, 3, 1, 2])
                strides = [1, 1, stride, stride]
            with self.test_scope():
                backprop = nn_ops.depthwise_conv2d_native_backprop_filter(
                    native_t0,
                    t1,
                    native_t2,
                    strides=strides,
                    padding=padding,
                    data_format=data_format)
        else:
            # For CPU, the format NCHW is not supported. Therefore we always use
            # NHWC here.
            backprop = nn_ops.depthwise_conv2d_native_backprop_filter(
                native_t0, t1, native_t2, strides=strides, padding=padding)
        ret = backprop.eval({t0: x0, t2: x2})
        self.assertShapeEqual(ret, backprop)
        exit(ret)

gpu_value = _GetVal(use_xla=True)
cpu_value = _GetVal(use_xla=False)
self.assertAllClose(cpu_value, gpu_value, rtol=1e-4, atol=1e-4)
