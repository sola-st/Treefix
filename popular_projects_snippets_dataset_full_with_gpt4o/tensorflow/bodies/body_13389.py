# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py

np.random.seed(42)
dense_numpy_array = np.random.rand(3, 3)
independent_dense_tf = constant_op.constant(
    dense_numpy_array, dtype='float32')

sp = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[4., 8.], dense_shape=[3, 3])
dense_of_sparse = sparse_ops.sparse_to_dense(sp.indices, sp.shape,
                                             sp.values)

result = sparse_ops.sparse_tensor_dense_matmul(
    independent_dense_tf, sp, adjoint_a=False, adjoint_b=False)
expected = math_ops.matmul(independent_dense_tf, dense_of_sparse)
self.assertAllEqual(expected, result)

result = sparse_ops.sparse_tensor_dense_matmul(
    independent_dense_tf, sp, adjoint_a=False, adjoint_b=True)
expected = math_ops.matmul(independent_dense_tf,
                           array_ops.transpose(dense_of_sparse))
self.assertAllEqual(expected, result)

result = sparse_ops.sparse_tensor_dense_matmul(
    independent_dense_tf, sp, adjoint_a=True, adjoint_b=False)
expected = math_ops.matmul(
    array_ops.transpose(independent_dense_tf), dense_of_sparse)
self.assertAllEqual(expected, result)

result = sparse_ops.sparse_tensor_dense_matmul(
    independent_dense_tf, sp, adjoint_a=True, adjoint_b=True)
expected = math_ops.matmul(
    array_ops.transpose(independent_dense_tf),
    array_ops.transpose(dense_of_sparse))
self.assertAllEqual(expected, result)
