# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
with self.session():
    sp_input = self._SparseTensor_4x6()
    sparse_tensor0 = sparse_ops.sparse_slice(sp_input, [0, 0], [4, 2])
    sparse_tensor1 = sparse_ops.sparse_slice(sp_input, [0, 2], [5, 2])
    sparse_tensor2 = sparse_ops.sparse_slice(sp_input, [0, 4], [5, 3])

    self.assertAllEqual(sparse_tensor0.indices,
                        [[0, 0], [1, 1], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensor0.values, [0, 11, 20, 30])
    self.assertAllEqual(sparse_tensor0.dense_shape, [4, 2])
    self.assertAllEqual(sparse_tensor1.indices,
                        [[0, 0], [1, 1], [2, 1], [3, 0], [3, 1]])
    self.assertAllEqual(sparse_tensor1.values, [2, 13, 23, 32, 33])
    self.assertAllEqual(sparse_tensor1.dense_shape, [4, 2])
    self.assertAllEqual(sparse_tensor2.indices,
                        [[0, 0], [0, 1], [1, 0], [2, 1], [3, 1]])
    self.assertAllEqual(sparse_tensor2.values, [4, 5, 14, 25, 35])
    self.assertAllEqual(sparse_tensor2.dense_shape, [4, 2])
