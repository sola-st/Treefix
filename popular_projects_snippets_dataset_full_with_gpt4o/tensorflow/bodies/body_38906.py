# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
# NOTE: This input is intentionally not sorted to validate the
# already_sorted flag below.
ind = np.array([[0, 0], [1, 0], [1, 2], [2, 0], [2, 1], [1, 1]])
# NB: these are not sorted
indices = np.array([0, 13, 10, 33, 32, 14])
values = np.array([-3, 4, 1, 9, 5, 1])
shape = np.array([3, 3])
indices = sparse_tensor.SparseTensorValue(
    np.array(ind, np.int64),
    np.array(indices, indices_dtype), np.array(shape, np.int64))
values = sparse_tensor.SparseTensorValue(
    np.array(ind, np.int64),
    np.array(values, values_dtype), np.array(shape, np.int64))
exit((indices, values))
