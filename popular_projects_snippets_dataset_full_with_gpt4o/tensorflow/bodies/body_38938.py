# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
sp_input = self._SparseTensor_2x5x6()
new_shape = np.array([3, 7, 5], dtype=np.int64)

with self.assertRaisesRegex(ValueError, "should have dimension sizes"):
    sparse_ops.sparse_reset_shape(sp_input, new_shape)
