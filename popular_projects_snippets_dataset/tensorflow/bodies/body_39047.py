# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
ind = np.array([[0, 0], [1, 0], [1, 2], [1, 3], [2, 2],
                [2, 3]]).astype(np.int64)
val = np.array([0, 10, 13, 14, 32, 33]).astype(np.int32)

ind = ind[permutation]
val = val[permutation]

shape = np.array([3, 4]).astype(np.int64)
exit(sparse_tensor_lib.SparseTensorValue(ind, val, shape))
