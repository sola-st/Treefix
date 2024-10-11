# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
self.assertTrue(isinstance(result_tensor, sparse_tensor.SparseTensor))
self.assertTrue(isinstance(input_sp_t, sparse_tensor.SparseTensor))
self.assertAllCloseAccordingToType(input_sp_t.indices,
                                   result_tensor.indices)
self.assertAllCloseAccordingToType(input_sp_t.dense_shape,
                                   result_tensor.dense_shape)

res_densified = sparse_ops.sparse_to_dense(
    result_tensor.indices, result_tensor.dense_shape, result_tensor.values)
self.assertAllCloseAccordingToType(result_np, res_densified)
