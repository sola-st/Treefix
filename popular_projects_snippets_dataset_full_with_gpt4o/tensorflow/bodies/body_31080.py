# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
pseudo_random = True
overlapping = True
pooling_ratio = [1, math.sqrt(3), math.sqrt(2), 1]
for num_batches in [1, 2]:
    for num_rows in [5, 13]:
        for num_cols in [5, 11]:
            for num_channels in [1, 3]:
                input_shape = (num_batches, num_rows, num_cols, num_channels)
                input_data = self._GenerateRandomInputTensor(input_shape)
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
