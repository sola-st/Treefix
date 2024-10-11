# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# double datatype is currently not supported for pooling ops
# on the ROCm platform
for dtype in [np.float32, np.float16
             ] + [np.float64] if not test.is_built_with_rocm() else []:
    tensor_input = np.random.rand(*input_shape).astype(dtype)
    with self.cached_session():
        t = constant_op.constant(tensor_input, shape=input_shape)
        out_op, _ = nn_ops.max_pool_with_argmax(t, ksize, strides, padding)
        gpu_val = self.evaluate(out_op)
    with self.cached_session(use_gpu=False):
        t = constant_op.constant(tensor_input, shape=input_shape)
        out_op = nn_ops.max_pool(t, ksize, strides, padding)
        cpu_val = self.evaluate(out_op)
    self.assertAllCloseAccordingToType(cpu_val, gpu_val)
