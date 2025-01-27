# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
with self.session():
    sp_input = self._SparseTensor_5x7()
    sp_tensor0 = sparse_ops.sparse_slice(sp_input, [0, 0], [5, 3])
    sp_tensor1 = sparse_ops.sparse_slice(sp_input, [0, 3], [5, 2])
    sp_tensor2 = sparse_ops.sparse_slice(sp_input, [0, 5], [5, 2])

    self.assertAllEqual(
        sp_tensor0.indices,
        [[0, 0], [0, 2], [1, 1], [2, 0], [3, 0], [3, 2], [4, 1]])
    self.assertAllEqual(sp_tensor0.values, [0, 2, 11, 20, 30, 32, 41])
    self.assertAllEqual(sp_tensor0.dense_shape, [5, 3])
    self.assertAllEqual(sp_tensor1.indices,
                        [[0, 1], [1, 0], [1, 1], [2, 0], [3, 0], [4, 1]])
    self.assertAllEqual(sp_tensor1.values, [4, 13, 14, 23, 33, 44])
    self.assertAllEqual(sp_tensor1.dense_shape, [5, 2])
    self.assertAllEqual(sp_tensor2.indices,
                        [[0, 0], [1, 1], [2, 0], [3, 0], [4, 1]])
    self.assertAllEqual(sp_tensor2.values, [5, 16, 25, 35, 46])
    self.assertAllEqual(sp_tensor2.dense_shape, [5, 2])

    sp_tensor0 = sparse_ops.sparse_slice(sp_input, [0, 0], [5, 2])
    sp_tensor1 = sparse_ops.sparse_slice(sp_input, [0, 2], [5, 2])
    sp_tensor2 = sparse_ops.sparse_slice(sp_input, [0, 4], [5, 2])
    sp_tensor3 = sparse_ops.sparse_slice(sp_input, [0, 6], [5, 2])
    self.assertAllEqual(sp_tensor0.indices,
                        [[0, 0], [1, 1], [2, 0], [3, 0], [4, 1]])
    self.assertAllEqual(sp_tensor0.values, [0, 11, 20, 30, 41])
    self.assertAllEqual(sp_tensor0.dense_shape, [5, 2])
    self.assertAllEqual(sp_tensor1.indices,
                        [[0, 0], [1, 1], [2, 1], [3, 0], [3, 1]])
    self.assertAllEqual(sp_tensor1.values, [2, 13, 23, 32, 33])
    self.assertAllEqual(sp_tensor1.dense_shape, [5, 2])
    self.assertAllEqual(sp_tensor2.indices,
                        [[0, 0], [0, 1], [1, 0], [2, 1], [3, 1], [4, 0]])
    self.assertAllEqual(sp_tensor2.values, [4, 5, 14, 25, 35, 44])
    self.assertAllEqual(sp_tensor2.dense_shape, [5, 2])
    self.assertAllEqual(sp_tensor3.indices, [[1, 0], [4, 0]])
    self.assertAllEqual(sp_tensor3.values, [16, 46])
    self.assertAllEqual(sp_tensor3.dense_shape, [5, 1])
