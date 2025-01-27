# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
input_shape = (1, 17, 23, 1)
input_data = self._GenerateRandomInputTensor(input_shape)
pooling_ratio = (1, math.sqrt(13), math.sqrt(7), 1)
output_shape = [int(a / b) for a, b in zip(input_shape, pooling_ratio)]
overlapping = True
pseudo_random = False

with self.cached_session() as _:
    input_tensor = constant_op.constant(input_data, shape=input_shape)
    output_tensor, unused_a, unused_b = nn_ops.fractional_avg_pool_v2(
        input_tensor,
        pooling_ratio,
        pseudo_random=pseudo_random,
        overlapping=overlapping,
        seed=self._SEED)
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
