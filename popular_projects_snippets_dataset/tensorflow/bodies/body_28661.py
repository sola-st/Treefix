# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self._testDatasetSpec(
    sparse_tensor.SparseTensor(
        indices=[[0]],
        values=constant_op.constant([0], dtype=dtypes.int32),
        dense_shape=[1]), sparse_tensor.SparseTensorSpec([1], dtypes.int32))
