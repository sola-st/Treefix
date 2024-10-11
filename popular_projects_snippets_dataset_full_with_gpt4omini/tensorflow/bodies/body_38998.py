# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
# Public API call to sparse-dense add.
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            expected_error):
    a = sparse_tensor.SparseTensor(a_indices, a_values, a_shape)
    self.evaluate(sparse_ops.sparse_add(a, b))
# Directly call generated kernel, by-passing SparseTensor validation.
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            expected_error):
    self.evaluate(
        sparse_ops.gen_sparse_ops.sparse_tensor_dense_add(
            a_indices, a_values, a_shape, b))
