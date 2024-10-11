# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
pool_func = gen_nn_ops.max_pool_v2 if v2 else nn_ops.max_pool
with self.cached_session(use_gpu=use_gpu):
    input_tensor = variables.Variable(
        np.array(input_data, dtype=np.float32).reshape(input_sizes))
    self.evaluate(variables.global_variables_initializer())
    output_tensor = pool_func(input_tensor, [1, window_rows, window_cols, 1],
                              [1, row_stride, col_stride, 1], padding)
    output_backprop_tensor = constant_op.constant(
        output_backprop, shape=output_sizes)

    input_backprop_tensor = self._MaxPoolGrad(
        input_tensor, output_tensor, output_backprop_tensor, window_rows,
        window_cols, row_stride, col_stride, padding, v2)

    actual_input_backprop = self.evaluate(input_backprop_tensor)
    self.assertShapeEqual(actual_input_backprop, input_backprop_tensor)
    actual_input_backprop = actual_input_backprop.flatten()
    actual_input_backprop = self._GetNdArray(actual_input_backprop)

    actual_output = self.evaluate(output_tensor).flatten()
    actual_output = self._GetNdArray(actual_output)

    self.assertAllClose(
        expected_input_backprop, actual_input_backprop, rtol=1e-6, atol=1e-6)
