# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
with self.session():
    sp_input = self._SparseTensor_4x6()
    sp_tensor0 = sparse_ops.sparse_slice(sp_input, [0, 0], [2, 6])
    sp_tensor1 = sparse_ops.sparse_slice(sp_input, [2, 0], [3, 7])
    self.assertAllEqual(
        sp_tensor0.indices,
        [[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4]])
    self.assertAllEqual(sp_tensor0.values, [0, 2, 4, 5, 11, 13, 14])
    self.assertAllEqual(sp_tensor0.dense_shape, [2, 6])
    self.assertAllEqual(
        sp_tensor1.indices,
        [[0, 0], [0, 3], [0, 5], [1, 0], [1, 2], [1, 3], [1, 5]])
    self.assertAllEqual(sp_tensor1.values, [20, 23, 25, 30, 32, 33, 35])
    self.assertAllEqual(sp_tensor1.dense_shape, [2, 6])
