# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    sp_input = sparse_tensor.SparseTensor(
        indices=np.array([[1, 2], [1, 3], [99, 1], [99, 3]]),
        values=np.array([1, 3, 2, 4]),
        dense_shape=np.array([2, 5]))

    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                r"indices\(2, 0\) is invalid"):
        self.evaluate(sparse_ops.sparse_fill_empty_rows(sp_input, -1))
