# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
val = np.array([0, 10, 13, 14, 32, 33])
shape = np.array([5, 6])
exit(sparse_tensor.SparseTensorValue(
    np.array(ind, np.int64),
    np.array(val, np.int32), np.array(shape, np.int64)))
