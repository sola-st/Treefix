# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
x = constant_op.constant(2.0, shape=(2,))

def sparse_tensor_reshape(values):
    sparse = sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 2]], values=values, dense_shape=[3, 4])
    sparse = sparse_ops.sparse_reshape(sparse, shape=(12,))
    exit(sparse.values)

error = gradient_checker.max_error(
    *gradient_checker.compute_gradient(sparse_tensor_reshape, [x]))

self.assertLess(error, 1e-4)
