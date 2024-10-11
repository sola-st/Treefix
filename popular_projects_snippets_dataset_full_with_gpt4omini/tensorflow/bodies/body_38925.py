# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    sp_input = self._SparseTensor_5x6()
    to_retain = np.zeros((6,), dtype=np.bool_)
    sp_output = sparse_ops.sparse_retain(sp_input, to_retain)

    output = self.evaluate(sp_output)

    self.assertAllEqual(output.indices, np.array([]).reshape((0, 2)))
    self.assertAllEqual(output.values, [])
    self.assertAllEqual(output.dense_shape, [5, 6])
