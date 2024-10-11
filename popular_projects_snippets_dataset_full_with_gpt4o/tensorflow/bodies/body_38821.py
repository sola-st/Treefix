# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for axis in (0, -2):
    sp_tensors_2 = self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_5x7(), num_split=2, axis=axis))
    self.assertAllEqual(sp_tensors_2[0].indices,
                        [[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3],
                         [1, 4], [1, 6], [2, 0], [2, 3], [2, 5]])
    self.assertAllEqual(sp_tensors_2[0].values,
                        [0, 2, 4, 5, 11, 13, 14, 16, 20, 23, 25])
    self.assertAllEqual(sp_tensors_2[0].dense_shape, [3, 7])
    self.assertAllEqual(
        sp_tensors_2[1].indices,
        [[0, 0], [0, 2], [0, 3], [0, 5], [1, 1], [1, 4], [1, 6]])
    self.assertAllEqual(sp_tensors_2[1].values, [30, 32, 33, 35, 41, 44, 46])
    self.assertAllEqual(sp_tensors_2[1].dense_shape, [2, 7])
    self.assertAllEqual(len(sp_tensors_2), 2)
    sp_tensors_3 = sparse_ops.sparse_split(
        sp_input=self._SparseTensor_5x7(), num_split=3, axis=axis)
    self.assertAllEqual(len(sp_tensors_3), 3)
    self.assertAllEqual(
        sp_tensors_3[0].indices,
        [[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4], [1, 6]])
    self.assertAllEqual(sp_tensors_3[0].values, [0, 2, 4, 5, 11, 13, 14, 16])
    self.assertAllEqual(sp_tensors_3[0].dense_shape, [2, 7])

    self.assertAllEqual(sp_tensors_3[1].values, [20, 23, 25, 30, 32, 33, 35])
    self.assertAllEqual(sp_tensors_3[1].dense_shape, [2, 7])
    self.assertAllEqual(sp_tensors_3[2].indices, [[0, 1], [0, 4], [0, 6]])
    self.assertAllEqual(sp_tensors_3[2].values, [41, 44, 46])
    self.assertAllEqual(sp_tensors_3[2].dense_shape, [1, 7])
