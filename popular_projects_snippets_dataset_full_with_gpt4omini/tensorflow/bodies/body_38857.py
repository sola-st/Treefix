# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
with self.session():
    sp_input = self._SparseTensor_4x6()
    sparse_tensor0 = sparse_ops.sparse_slice(sp_input, [0, 0], [4, 1])
    sparse_tensor1 = sparse_ops.sparse_slice(sp_input, [0, 1], [4, 1])
    sparse_tensor2 = sparse_ops.sparse_slice(sp_input, [0, 2], [4, 1])
    sparse_tensor3 = sparse_ops.sparse_slice(sp_input, [0, 3], [4, 1])
    sparse_tensor4 = sparse_ops.sparse_slice(sp_input, [0, 4], [5, 1])
    sparse_tensor5 = sparse_ops.sparse_slice(sp_input, [0, 5], [6, 3])
    self.assertAllEqual(sparse_tensor0.indices, [[0, 0], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensor0.values, [0, 20, 30])
    self.assertAllEqual(sparse_tensor0.dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensor1.indices, [[1, 0]])
    self.assertAllEqual(sparse_tensor1.values, [11])
    self.assertAllEqual(sparse_tensor1.dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensor2.indices, [[0, 0], [3, 0]])
    self.assertAllEqual(sparse_tensor2.values, [2, 32])
    self.assertAllEqual(sparse_tensor2.dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensor3.indices, [[1, 0], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensor3.dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensor3.values, [13, 23, 33])
    self.assertAllEqual(sparse_tensor4.indices, [[0, 0], [1, 0]])
    self.assertAllEqual(sparse_tensor4.values, [4, 14])
    self.assertAllEqual(sparse_tensor4.dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensor5.indices, [[0, 0], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensor5.values, [5, 25, 35])
    self.assertAllEqual(sparse_tensor5.dense_shape, [4, 1])
