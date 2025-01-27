# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    sp_input = self._SparseTensor_2x5x6_Empty()
    sp_output = sparse_ops.sparse_reset_shape(sp_input)

    output = self.evaluate(sp_output)

    self.assertAllEqual(output.indices.shape, [0, 3])
    self.assertAllEqual(output.values.shape, [0])
    self.assertAllEqual(output.dense_shape, [0, 0, 0])
