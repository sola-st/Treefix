# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for axis in (1, -1):
    sparse_tensors = self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_4x6(), num_split=6, axis=axis))
    self.assertAllEqual(len(sparse_tensors), 6)
    self.assertAllEqual(sparse_tensors[0].indices, [[0, 0], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensors[0].values, [0, 20, 30])
    self.assertAllEqual(sparse_tensors[0].dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensors[1].indices, [[1, 0]])
    self.assertAllEqual(sparse_tensors[1].values, [11])
    self.assertAllEqual(sparse_tensors[1].dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensors[2].indices, [[0, 0], [3, 0]])
    self.assertAllEqual(sparse_tensors[2].values, [2, 32])
    self.assertAllEqual(sparse_tensors[2].dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensors[3].indices, [[1, 0], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensors[3].dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensors[3].values, [13, 23, 33])
    self.assertAllEqual(sparse_tensors[4].indices, [[0, 0], [1, 0]])
    self.assertAllEqual(sparse_tensors[4].values, [4, 14])
    self.assertAllEqual(sparse_tensors[4].dense_shape, [4, 1])
    self.assertAllEqual(sparse_tensors[5].indices, [[0, 0], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensors[5].values, [5, 25, 35])
    self.assertAllEqual(sparse_tensors[5].dense_shape, [4, 1])
