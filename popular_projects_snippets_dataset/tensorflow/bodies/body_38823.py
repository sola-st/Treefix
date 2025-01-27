# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for axis in (1, -1):
    sparse_tensors = self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_4x6(), num_split=3, axis=axis))
    self.assertAllEqual(len(sparse_tensors), 3)
    self.assertAllEqual(sparse_tensors[0].indices,
                        [[0, 0], [1, 1], [2, 0], [3, 0]])
    self.assertAllEqual(sparse_tensors[0].values, [0, 11, 20, 30])
    self.assertAllEqual(sparse_tensors[0].dense_shape, [4, 2])
    self.assertAllEqual(sparse_tensors[1].indices,
                        [[0, 0], [1, 1], [2, 1], [3, 0], [3, 1]])
    self.assertAllEqual(sparse_tensors[1].values, [2, 13, 23, 32, 33])
    self.assertAllEqual(sparse_tensors[1].dense_shape, [4, 2])
    self.assertAllEqual(sparse_tensors[2].indices,
                        [[0, 0], [0, 1], [1, 0], [2, 1], [3, 1]])
    self.assertAllEqual(sparse_tensors[2].values, [4, 5, 14, 25, 35])
    self.assertAllEqual(sparse_tensors[2].dense_shape, [4, 2])
