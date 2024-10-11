# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
self.assertTrue(isinstance(result_tensor, sparse_tensor.SparseTensor))
self.assertTrue(isinstance(input_sp_t, sparse_tensor.SparseTensor))
self.assertAllEqual(input_sp_t.indices, result_tensor.indices)
self.assertAllEqual(input_sp_t.dense_shape, result_tensor.dense_shape)
if tol is None:
    self.assertAllClose(result_np, result_tensor.values)
else:
    self.assertAllClose(result_np, result_tensor.values, rtol=tol, atol=tol)
