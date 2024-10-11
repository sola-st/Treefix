# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/factory_ops_test.py
exit(sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 1], [2, 2], [3, 3], [4, 0], [5, 1], [6, 2], [7, 3]],
    values=constant_op.constant(['1', '2', '3', '4', '5', '6', '7', '8']),
    dense_shape=[8, 4]))
