# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    sp_input = self._SparseTensor_2x3x4(dtypes.int64)
    output = sparse_ops.sparse_to_indicator(sp_input, 200)

    expected_output = np.zeros((2, 3, 200), dtype=np.bool_)
    expected_trues = [(0, 0, 1), (0, 1, 10), (0, 1, 12), (1, 0, 103),
                      (1, 1, 149), (1, 1, 150), (1, 2, 122)]
    for expected_true in expected_trues:
        expected_output[expected_true] = True

    self.assertAllEqual(output, expected_output)
