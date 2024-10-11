# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
exit(sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 1]], values=(i * [1, -1]), dense_shape=[2, 2]))
