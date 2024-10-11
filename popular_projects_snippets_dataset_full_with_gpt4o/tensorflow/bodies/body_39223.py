# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# [    1]
# [2    ]
# [3   4]
ind = np.array([[0, 2], [1, 0], [2, 0], [2, 2]])
val = np.array([1, 2, 3, 4])
shape = np.array([3, 3])
exit(sparse_tensor.SparseTensorValue(
    np.array(ind, np.int64),
    np.array(val, np.float32), np.array(shape, np.int64)))
