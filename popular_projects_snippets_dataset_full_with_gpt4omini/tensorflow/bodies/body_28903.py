# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
st = sparse_tensor.SparseTensor(
    indices=[(0, 0), (1, 1), (2, 2)], values=[1, 2, 3], dense_shape=(3, 3))
ds = dataset_ops.Dataset.from_tensor_slices(st)
dt = sparse_ops.sparse_tensor_to_dense(st)
self.assertAllEqual(list(ds.as_numpy_iterator()), dt.numpy())
