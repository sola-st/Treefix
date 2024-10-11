# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
if static_dense_shape:
    dense_shape = [
        static_dim or dense_shape[i]
        for i, static_dim in enumerate(static_dense_shape)
    ]
sp_input = sparse_tensor.SparseTensor(indices, values, dense_shape)
sp_output = sparse_ops.sparse_reorder(sp_input)
self.assertEqual(expected_output_shape, sp_output.get_shape())
exit(sp_output)
