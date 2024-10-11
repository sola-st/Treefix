# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
for num_batches in [1, 3]:
    for row_window_size in [2, 5]:
        for col_window_size in [2, 4]:
            num_rows = row_window_size * 5
            num_cols = col_window_size * 7
            for num_channels in [1, 2]:
                input_shape = (num_batches, num_rows, num_cols, num_channels)
                with self.cached_session() as _:
                    input_tensor = constant_op.constant(
                        self._GenerateRandomInputTensor(input_shape).astype(
                            np.float32))
                    window_size = [1, row_window_size, col_window_size, 1]
                    stride_size = [1, row_window_size, col_window_size, 1]
                    padding = "VALID"
                    output_tensor = nn_ops.avg_pool(input_tensor, window_size,
                                                    stride_size, padding)
                    output_data = self.evaluate(output_tensor)
                    num_elements = 1
                    for dim_size in output_data.shape:
                        num_elements *= dim_size
                    output_backprop = (self._PRNG.rand(num_elements) *
                                       1000).reshape(output_data.shape)
                    input_backprop_tensor = gen_nn_ops.avg_pool_grad(
                        input_tensor.get_shape(), output_backprop, window_size,
                        stride_size, padding)
                    input_backprop = self.evaluate(input_backprop_tensor)
                    row_seq = list(range(0, num_rows + 1, row_window_size))
                    col_seq = list(range(0, num_cols + 1, col_window_size))
                    fap_input_backprop_tensor = gen_nn_ops.fractional_avg_pool_grad(
                        input_tensor.get_shape(),
                        output_backprop,
                        row_seq,
                        col_seq,
                        overlapping=False)
                    fap_input_backprop = self.evaluate(fap_input_backprop_tensor)
                    self.assertShapeEqual(input_backprop, fap_input_backprop_tensor)
                    self.assertAllClose(input_backprop, fap_input_backprop)
