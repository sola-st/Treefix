# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
exit(sparse_tensor.SparseTensorValue(
    indices=[[0, 0], [1, 1]], values=(i * [1, -1]), dense_shape=[2, 2]))
