# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
exit(sparse_tensor.SparseTensor(
    indices=[[0]],
    values=constant_op.constant([0], dtype=dtypes.int32),
    dense_shape=[1]))
