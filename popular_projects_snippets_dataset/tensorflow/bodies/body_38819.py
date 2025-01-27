# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for axis in (0, -2):
    sp_tensors = self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_4x6(), num_split=2, axis=axis))
    self.assertAllEqual(len(sp_tensors), 2)
    self.assertAllEqual(
        sp_tensors[0].indices,
        [[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4]])
    self.assertAllEqual(sp_tensors[0].values, [0, 2, 4, 5, 11, 13, 14])
    self.assertAllEqual(sp_tensors[0].dense_shape, [2, 6])
    self.assertAllEqual(
        sp_tensors[1].indices,
        [[0, 0], [0, 3], [0, 5], [1, 0], [1, 2], [1, 3], [1, 5]])
    self.assertAllEqual(sp_tensors[1].values, [20, 23, 25, 30, 32, 33, 35])
    self.assertAllEqual(sp_tensors[1].dense_shape, [2, 6])
