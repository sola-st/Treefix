# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
if np.__version__ == "1.13.0":
    self.skipTest("numpy 1.13.0 bug")

with test_util.force_cpu():
    np.random.seed(1618)
    shapes = [np.random.randint(1, 10, size=rank) for rank in range(1, 6)]
    for shape in shapes:
        for dtype in [np.int32, np.int64, np.float32, np.float64]:
            dn_input = np.random.randn(*shape).astype(dtype)
            rank = self.evaluate(array_ops.rank(dn_input))
            perm = np.random.choice(rank, rank, False)
            sp_input, unused_a_nnz = _sparsify(dn_input)
            sp_trans = sparse_ops.sparse_transpose(sp_input, perm=perm)
            dn_trans = sparse_ops.sparse_tensor_to_dense(sp_trans)
            expected_trans = array_ops.transpose(dn_input, perm=perm)
            self.assertAllEqual(expected_trans.shape, sp_trans.get_shape())
            self.assertAllEqual(dn_trans, expected_trans)
