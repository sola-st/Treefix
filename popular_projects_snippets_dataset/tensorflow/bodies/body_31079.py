# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
input_shape = (1, 7, 13, 1)
input_data = self._GenerateRandomInputTensor(input_shape)
pooling_ratio = [1, math.sqrt(2), math.sqrt(3), 1]

for pseudo_random in True, False:
    for overlapping in True, False:
        with self.cached_session() as _:
            input_tensor = constant_op.constant(input_data, shape=input_shape)
            output_tensor, unused_a, unused_b = nn_ops.fractional_avg_pool_v2(
                input_tensor,
                pooling_ratio,
                pseudo_random=pseudo_random,
                overlapping=overlapping,
                seed=self._SEED)
            output_data = self.evaluate(output_tensor)
            output_shape = output_data.shape
            # error_margin and delta setting is similar to avg_pool_grad.
            error_margin = 1e-4
            gradient_error = gradient_checker.compute_gradient_error(
                input_tensor,
                input_shape,
                output_tensor,
                output_shape,
                x_init_value=input_data.reshape(input_shape),
                delta=1e-2)
            self.assertLess(gradient_error, error_margin)
