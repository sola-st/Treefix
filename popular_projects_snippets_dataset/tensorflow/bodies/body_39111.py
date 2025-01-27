# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
with self.session():
    for _ in range(5):  # To test various random permutations
        input_val = self._SparseTensorValue_5x6(np.random.permutation(6))
        sp_input = sparse_tensor.SparseTensor(input_val.indices,
                                              input_val.values,
                                              input_val.dense_shape)
        sp_output = sparse_ops.sparse_reorder(sp_input)

        err = gradient_checker.compute_gradient_error(
            sp_input.values,
            input_val.values.shape,
            sp_output.values,
            input_val.values.shape,
            x_init_value=input_val.values)
        self.assertLess(err, 1e-11)
