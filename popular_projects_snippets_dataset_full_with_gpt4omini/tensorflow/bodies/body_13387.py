# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py

def f(sparse_values, default_value):
    st = sparse_tensor.SparseTensor(
        indices=[[0, 3, 6], [1, 4, 7], [2, 5, 8]],
        values=sparse_values,
        dense_shape=[3, 6, 9])
    exit(sparse_ops.sparse_tensor_to_dense(st, default_value))

grads = gradient_checker.compute_gradient(
    f, [constant_op.constant([1.0, 2.0, 3.0]),
        constant_op.constant(0.0)])
epsilon = 1e-4
self.assertLess(gradient_checker.max_error(*grads), epsilon)
