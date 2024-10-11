# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
with test_util.force_cpu():
    sp_a = self._SparseTensor_3x3()
    sp_b = self._SparseTensor_3x3(negate=True)

    sp_sum = sparse_ops.sparse_add(sp_a, sp_b, 0.1)
    sum_out = self.evaluate(sp_sum)

    self.assertEqual(sp_sum.dense_shape.get_shape(), [2])
    self.assertAllEqual(sum_out.indices, np.empty([0, 2]))
    self.assertAllEqual(sum_out.values, [])
    self.assertAllEqual(sum_out.dense_shape, [3, 3])
