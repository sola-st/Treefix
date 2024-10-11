# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
sp_input = self._SparseTensor_4x6(val_dtype=np.float32)
start_and_size = [([0, 0], [4, 2]),
                  ([0, 2], [5, 2]),
                  ([0, 4], [5, 3])]

with self.session():
    for start, size in start_and_size:
        sp_output = sparse_ops.sparse_slice(sp_input, start, size)
        nnz_in = len(self.evaluate(sp_input.values))
        nnz_out = len(self.evaluate(sp_output.values))

        err = gradient_checker.compute_gradient_error(
            [sp_input.values], [(nnz_in,)], sp_output.values, (nnz_out,))
        self.assertLess(err, 1e-3)
