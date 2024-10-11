# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    # Identity(2) + AllOnes(2,2).  Should be equal to 2 * Identity(2).
    indices = [[0, 0], [1, 1]]
    vals = [1, 1]
    shape = (2, 2)

    sp_t = sparse_tensor.SparseTensor(indices, vals, shape)
    dense_t = array_ops.ones(shape, dtype=dtypes.int32)
    self._check(
        sparse_ops.sparse_dense_cwise_add(sp_t, dense_t),
        np.identity(2) * 2, sp_t)

    # Variant of above, but broadcasts the dense side.
    dense_t = array_ops.ones([1], dtype=dtypes.int32)
    self._check(
        sparse_ops.sparse_dense_cwise_add(sp_t, dense_t),
        np.identity(2) * 2, sp_t)
