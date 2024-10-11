# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
if test.is_gpu_available(cuda_only=True):
    try:
        config_exec.enable_op_determinism()
        orig_input = [
            1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 1.0, 0.0, 1.0
        ]
        tensor_input = [11.0, 12.0, 13.0, 14.0, 21.0, 22.0, 23.0, 24.0]

        with GetDeviceScope(self, True):
            orig_in = constant_op.constant(orig_input, shape=[2, 3, 3, 1])
            t = constant_op.constant(tensor_input, shape=[2, 2, 2, 1])
            argmax_t = constant_op.constant(
                [0, 1, 3, 5, 0, 2, 6, 8], shape=[2, 2, 2, 1], dtype=dtypes.int64)
            with self.assertRaisesRegexp(
                errors_impl.UnimplementedError, "Determinism is not yet supported"
                " for MaxPoolGradWithArgmax."):
                out_op = gen_nn_ops.max_pool_grad_with_argmax(
                    orig_in,
                    t,
                    argmax_t,
                    ksize=[1, 2, 2, 1],
                    strides=[1, 1, 1, 1],
                    padding="VALID",
                    include_batch_in_index=False)
                self.evaluate(out_op)
    finally:
        config_exec.disable_op_determinism()
else:
    try:
        config_exec.enable_op_determinism()
        orig_input = [
            1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 1.0, 0.0, 1.0
        ]
        tensor_input = [11.0, 12.0, 13.0, 14.0, 21.0, 22.0, 23.0, 24.0]

        with GetDeviceScope(self, False):
            orig_in = constant_op.constant(orig_input, shape=[2, 3, 3, 1])
            t = constant_op.constant(tensor_input, shape=[2, 2, 2, 1])
            argmax_t = constant_op.constant(
                [0, 1, 3, 5, 0, 2, 6, 8], shape=[2, 2, 2, 1], dtype=dtypes.int64)
            out_op = gen_nn_ops.max_pool_grad_with_argmax(
                orig_in,
                t,
                argmax_t,
                ksize=[1, 2, 2, 1],
                strides=[1, 1, 1, 1],
                padding="VALID",
                include_batch_in_index=False)
            self.evaluate(out_op)
    finally:
        config_exec.disable_op_determinism()
