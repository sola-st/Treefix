# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_d9m_test.py
with self.cached_session():
    for large_batch in [False, True]:
        for x_dtype in [dtypes.float16, dtypes.float32]:  # skipping bfloat16
            x, scale, offset, mean, variance, _ = self._genParams(
                data_format, x_dtype, large_batch)
            for is_training in [False, True]:
                op_output = nn_impl.fused_batch_norm(
                    x,
                    scale,
                    offset,
                    mean,
                    variance,
                    data_format=data_format,
                    is_training=is_training,
                    exponential_avg_factor=1.01)
                y_a, running_mean_a, running_var_a = op_output
                y_a = self.evaluate(y_a)
                if is_training:
                    running_mean_a = self.evaluate(running_mean_a)
                    running_var_a = self.evaluate(running_var_a)
                for _ in range(5):
                    op_output_b = nn_impl.fused_batch_norm(
                        x,
                        scale,
                        offset,
                        mean,
                        variance,
                        data_format=data_format,
                        is_training=is_training,
                        exponential_avg_factor=1.01)
                    y_b, running_mean_b, running_var_b = op_output_b
                    y_b = self.evaluate(y_b)
                    self.assertAllEqual(y_a, y_b)
                    if is_training:
                        running_mean_b = self.evaluate(running_mean_b)
                        running_var_b = self.evaluate(running_var_b)
                        self.assertAllEqual(running_mean_a, running_mean_b)
                        self.assertAllEqual(running_var_a, running_var_b)
