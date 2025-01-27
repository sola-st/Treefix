# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# Test case for GitHub 21964.
x = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 1]], values=[1, 2], dense_shape=[2, 2])
y = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 1]], values=[1, 2], dense_shape=[2, 2])
z = sparse_ops.sparse_concat(-1, [x, y])
self.assertEqual(z.get_shape().as_list(), [2, 4])
