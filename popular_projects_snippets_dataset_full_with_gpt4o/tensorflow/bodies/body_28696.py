# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
# pylint: disable=g-complex-comprehension
indices = np.array(
    [[i, j] for i in range(len(slices)) for j in range(len(slices[i]))],
    dtype=np.int64)
values = np.array([val for s in slices for val in s], dtype=np.float64)
# pylint: enable=g-complex-comprehension
dense_shape = np.array(
    [len(slices), max(len(s) for s in slices) + 1], dtype=np.int64)
sparse_components = sparse_tensor.SparseTensor(indices, values, dense_shape)
exit(dataset_ops.Dataset.from_sparse_tensor_slices(sparse_components))
