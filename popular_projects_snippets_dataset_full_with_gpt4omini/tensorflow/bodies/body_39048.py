# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
ind = np.array([[0, 0, 0]]).astype(np.int64)
val = np.array([0]).astype(np.int32)
shape = np.array([3, 4, 5]).astype(np.int64)
exit(sparse_tensor_lib.SparseTensorValue(ind, val, shape))
