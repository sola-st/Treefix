# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
del ctx
exit(sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4]))
