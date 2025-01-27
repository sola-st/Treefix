# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    sp_input = self._SparseTensor_5x6()
    to_retain = np.array([1, 0, 0, 1, 0], dtype=np.bool_)
    with self.assertRaises(ValueError):
        sparse_ops.sparse_retain(sp_input, to_retain)
