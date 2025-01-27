# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for axis in (0, -2):
    sp_tensors = self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_4x6(), num_split=4, axis=axis))
    self.assertAllEqual(len(sp_tensors), 4)
    self.assertAllEqual(sp_tensors[0].indices,
                        [[0, 0], [0, 2], [0, 4], [0, 5]])
    self.assertAllEqual(sp_tensors[0].values, [0, 2, 4, 5])
    self.assertAllEqual(sp_tensors[0].dense_shape, [1, 6])
    self.assertAllEqual(sp_tensors[1].indices, [[0, 1], [0, 3], [0, 4]])
    self.assertAllEqual(sp_tensors[1].values, [11, 13, 14])
    self.assertAllEqual(sp_tensors[1].dense_shape, [1, 6])
    self.assertAllEqual(sp_tensors[2].indices, [[0, 0], [0, 3], [0, 5]])
    self.assertAllEqual(sp_tensors[2].values, [20, 23, 25])
    self.assertAllEqual(sp_tensors[2].dense_shape, [1, 6])
    self.assertAllEqual(sp_tensors[3].indices,
                        [[0, 0], [0, 2], [0, 3], [0, 5]])
    self.assertAllEqual(sp_tensors[3].values, [30, 32, 33, 35])
    self.assertAllEqual(sp_tensors[3].dense_shape, [1, 6])
