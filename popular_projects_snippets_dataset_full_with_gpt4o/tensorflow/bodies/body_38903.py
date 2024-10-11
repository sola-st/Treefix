# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    sp_input = self._SparseTensor_5x6(dtypes.int32)
    output = sparse_ops.sparse_to_indicator(sp_input, 50)

    expected_output = np.zeros((5, 50), dtype=np.bool_)
    expected_trues = ((0, 0), (1, 10), (1, 13), (1, 14), (3, 32), (3, 33))
    for expected_true in expected_trues:
        expected_output[expected_true] = True

    self.assertAllEqual(output, expected_output)
