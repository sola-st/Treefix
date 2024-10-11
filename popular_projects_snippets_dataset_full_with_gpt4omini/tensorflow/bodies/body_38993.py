# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
with test_util.force_cpu():
    sp_a = self._SparseTensor_3x3()
    sp_b = self._SparseTensor_3x3_v2()

    # sum:
    # [       2]
    # [.1      ]
    # [ 6   -.2]

    # two values should vanish: |.1| < .21, and |-.2| < .21
    sp_sum = sparse_ops.sparse_add(sp_a, sp_b, thresh=0.21)
    sum_out = self.evaluate(sp_sum)

    self.assertEqual(sp_sum.dense_shape.get_shape(), [2])
    self.assertAllEqual(sum_out.indices, [[0, 1], [2, 0]])
    self.assertAllEqual(sum_out.values, [2, 6])
    self.assertAllEqual(sum_out.dense_shape, [3, 3])

    # only .1 vanishes
    sp_sum = sparse_ops.sparse_add(sp_a, sp_b, thresh=0.11)
    sum_out = self.evaluate(sp_sum)

    self.assertEqual(sp_sum.dense_shape.get_shape(), [2])
    self.assertAllEqual(sum_out.indices, [[0, 1], [2, 0], [2, 1]])
    self.assertAllClose(sum_out.values, [2, 6, -.2])
    self.assertAllEqual(sum_out.dense_shape, [3, 3])
