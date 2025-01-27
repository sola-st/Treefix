# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
ind = np.empty(shape=(0, 2), dtype=np.int64)
val = np.array([]).astype(val_dtype)
shape = np.array([4, 6]).astype(np.int64)
exit(sparse_tensor.SparseTensor(ind, val, shape))
