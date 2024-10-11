# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
for num_batches in [1, 3]:
    for row_window_size in [2, 5]:
        for col_window_size in [2, 4]:
            num_rows = (row_window_size - 1) * 5 + 1
            num_cols = (col_window_size - 1) * 7 + 1
            for num_channels in [1, 2]:
                input_shape = (num_batches, num_rows, num_cols, num_channels)
                with self.cached_session() as _:
                    input_tensor = constant_op.constant(
                        self._GenerateUniqueRandomInputTensor(input_shape))
                    window_size = [1, row_window_size, col_window_size, 1]
                    stride_size = [1, row_window_size - 1, col_window_size - 1, 1]
                    padding = "VALID"
                    output_tensor = nn_ops.max_pool(input_tensor, window_size,
                                                    stride_size, padding)
                    output_data = self.evaluate(output_tensor)
                    output_backprop = self._PRNG.randint(100, size=output_data.shape)
                    input_backprop_tensor = gen_nn_ops.max_pool_grad(
                        input_tensor, output_tensor, output_backprop, window_size,
                        stride_size, padding)
                    input_backprop = self.evaluate(input_backprop_tensor)
                    row_seq = list(range(0, num_rows, row_window_size - 1))
                    col_seq = list(range(0, num_cols, col_window_size - 1))
                    row_seq[-1] += 1
                    col_seq[-1] += 1
                    fmp_input_backprop_tensor = gen_nn_ops.fractional_max_pool_grad(
                        input_tensor,
                        output_tensor,
                        output_backprop,
                        row_seq,
                        col_seq,
                        overlapping=True)
                    fmp_input_backprop = self.evaluate(fmp_input_backprop_tensor)
                    self.assertShapeEqual(input_backprop, fmp_input_backprop_tensor)
                    self.assertAllClose(input_backprop, fmp_input_backprop)
