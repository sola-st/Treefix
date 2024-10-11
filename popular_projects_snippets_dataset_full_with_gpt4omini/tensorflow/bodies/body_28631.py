# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset_fn = dataset_ops.Dataset.from_sparse_tensor_slices(
    sparse_tensor.SparseTensor(
        indices=np.array([[0, 0], [1, 0], [2, 0]]),
        values=np.array([0, 0, 0]),
        dense_shape=np.array([3, 1])))
self.assertEmpty(dataset_fn._inputs())
