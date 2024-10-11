# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
with test_util.force_cpu():
    for sp_a in (self._SparseTensorValue_3x3(), self._SparseTensor_3x3()):
        for sp_b in (self._SparseTensorValue_3x3(), self._SparseTensor_3x3()):
            sp_sum = sparse_ops.sparse_add(sp_a, sp_b)
            self.assertAllEqual((3, 3), sp_sum.get_shape())

            sum_out = self.evaluate(sp_sum)

            self.assertEqual(sp_sum.dense_shape.get_shape(), [2])
            self.assertAllEqual(sum_out.indices, [[0, 1], [1, 0], [2, 0], [2, 1]])
            self.assertAllEqual(sum_out.values, [2, 4, 6, 8])
            self.assertAllEqual(sum_out.dense_shape, [3, 3])
