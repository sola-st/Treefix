# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
# [0 |  |2 |  |4 |5 ]
# [  |11|  |13|14|  ]
# [20|  |  |23|  |25]
# [30|  |32|33|  |35]
ind = np.array([[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4],
                [2, 0], [2, 3], [2, 5], [3, 0], [3, 2], [3, 3],
                [3, 5]]).astype(np.int64)
val = np.array(
    [0, 2, 4, 5, 11, 13, 14, 20, 23, 25, 30, 32, 33, 35]).astype(np.int64)
shape = np.array([4, 6]).astype(np.int64)
exit(sparse_tensor.SparseTensor(ind, val, shape))
