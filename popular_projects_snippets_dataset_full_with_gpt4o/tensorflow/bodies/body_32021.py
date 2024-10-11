# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
x1 = np.random.rand(*filter_sizes)
x2 = np.random.rand(*output_sizes)
if isinstance(padding, list):
    padding = [(0, 0)] + padding + [(0, 0)]

def _GetVal(use_gpu, dtype):
    with self.cached_session(use_gpu=use_gpu):
        t0 = constant_op.constant(input_sizes, shape=[len(input_sizes)])
        t1 = constant_op.constant(x1, shape=filter_sizes, dtype=dtype)
        t2 = constant_op.constant(x2, shape=output_sizes, dtype=dtype)
        backprop = nn_ops.depthwise_conv2d_native_backprop_input(
            t0, t1, t2, strides=[1, stride, stride, 1], padding=padding)
        ret = self.evaluate(backprop)
        self.assertShapeEqual(ret, backprop)
        exit(ret)

rtol, atol = (1e-1, 1e-1) if dtype == "bfloat16" else (1e-4, 1e-4)
gpu_value = _GetVal(use_gpu=True, dtype=dtype)
cpu_value = _GetVal(use_gpu=False, dtype=dtype)
self.assertAllClose(cpu_value, gpu_value, rtol=rtol, atol=atol)
