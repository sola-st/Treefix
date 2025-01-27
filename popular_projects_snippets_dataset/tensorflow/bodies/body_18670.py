# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_d9m_test.py
with self.cached_session():
    for large_batch in [False, True]:
        # Only run with float32, as float16 is very slow on CPUs
        params = self._genParams(data_format, dtypes.float32, large_batch)
        x, scale, offset, mean, variance, upstream_gradients = params
        for is_training in [False, True]:
            for backprop_to in [x, scale, offset]:
                with backprop.GradientTape(persistent=True) as tape:
                    tape.watch(backprop_to)
                    op_output = nn_impl.fused_batch_norm(
                        x,
                        scale,
                        offset,
                        mean,
                        variance,
                        data_format=data_format,
                        is_training=is_training,
                        exponential_avg_factor=0.99)
                    gradient_injector_output = op_output[0] * upstream_gradients
                if (len(config.list_physical_devices('GPU')) and
                    not is_training):
                    # Only backprop to offset is nondeterministic (on GPU, when
                    # is_training=False), but backprop to the other parameters is
                    # calculated using the same kernel.
                    with self.assertRaisesRegex(
                        errors_impl.UnimplementedError,
                        'A deterministic GPU implementation of fused batch-norm' +
                        ' backprop, when training is disabled, is not currently' +
                        ' available.'):
                        grad = tape.gradient(gradient_injector_output, backprop_to)
                        self.evaluate(grad)
                else:
                    grad_a = tape.gradient(gradient_injector_output, backprop_to)
                    grad_a = self.evaluate(grad_a)
                    for _ in range(3):
                        grad_b = tape.gradient(gradient_injector_output,
                                               backprop_to)
                        grad_b = self.evaluate(grad_b)
                        self.assertAllEqual(grad_a, grad_b)
