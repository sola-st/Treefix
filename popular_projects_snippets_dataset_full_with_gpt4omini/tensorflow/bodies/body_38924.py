# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    for sp_input in (self._SparseTensorValue_5x6(), self._SparseTensor_5x6()):
        to_retain = np.array([1, 0, 0, 1, 1, 0], dtype=np.bool_)
        sp_output = sparse_ops.sparse_retain(sp_input, to_retain)

        output = self.evaluate(sp_output)

        self.assertAllEqual(output.indices, [[0, 0], [1, 4], [3, 2]])
        self.assertAllEqual(output.values, [0, 14, 32])
        self.assertAllEqual(output.dense_shape, [5, 6])
