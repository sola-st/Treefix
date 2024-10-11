# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# double datatype is currently not supported for pooling ops
# on the ROCm platform
for dtype in [np.float32, np.float16, dtypes.bfloat16.as_numpy_dtype
             ] + [np.float64] if not test.is_built_with_rocm() else []:
    # Generate numbers in a narrow range, so that there are many duplicates
    # in the input.
    tensor_input = np.random.random_integers(0, 3, input_shape).astype(dtype)
    tensor_output = np.random.rand(*output_shape).astype(dtype)
    with self.cached_session():
        t = constant_op.constant(tensor_input, shape=input_shape)
        _, argmax_op = nn_ops.max_pool_with_argmax(t, ksize, strides, padding)
        argmax = self.evaluate(argmax_op)
        grad_in = constant_op.constant(tensor_output, shape=output_shape)
        out_op = gen_nn_ops.max_pool_grad_with_argmax(t, grad_in, argmax, ksize,
                                                      strides, padding)
        gpu_val = self.evaluate(out_op)
        self.assertShapeEqual(gpu_val, out_op)
    with self.cached_session(use_gpu=False):
        t = constant_op.constant(tensor_input, shape=input_shape)
        out_op = nn_ops.max_pool(t, ksize, strides, padding)
        orig_out = self.evaluate(out_op)
        grad_in = constant_op.constant(tensor_output, shape=output_shape)
        out_op = gen_nn_ops.max_pool_grad(t, orig_out, grad_in, ksize, strides,
                                          padding)
        cpu_val = self.evaluate(out_op)
        self.assertShapeEqual(cpu_val, out_op)
    # The CPU version accumulates its gradient on fp16, so it's less
    # accurate than the GPU version that does the accumulation on fp32
    self.assertAllCloseAccordingToType(
        cpu_val,
        gpu_val,
        half_rtol=0.01,
        half_atol=0.01,
        bfloat16_rtol=0.02,
        bfloat16_atol=0.1)
