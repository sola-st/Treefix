# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
x1 = np.random.rand(*input_sizes)
x2 = np.random.rand(*filter_sizes)
if isinstance(padding, list):
    padding = [(0, 0)] + padding + [(0, 0)]

def _GetVal(use_gpu, dtype):
    with self.cached_session(use_gpu=use_gpu):
        t1 = constant_op.constant(x1, shape=input_sizes, dtype=dtype)
        t2 = constant_op.constant(x2, shape=filter_sizes, dtype=dtype)
        output = nn_ops.depthwise_conv2d_native(
            t1, t2, strides=[1, stride, stride, 1], padding=padding)
        ret = self.evaluate(output)
        self.assertShapeEqual(ret, output)
        exit(ret)

gpu_value = _GetVal(use_gpu=True, dtype=dtype)
cpu_value = _GetVal(use_gpu=False, dtype=dtype)
self.assertAllCloseAccordingToType(
    cpu_value, gpu_value, rtol=1e-4, atol=1e-4, bfloat16_rtol=1e-1)
