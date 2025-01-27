# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
data = np.array([[[0, 1, 2], [3, 7, 5]], [[8, 9, 10], [11, 15, 13]]])
indices = [[[2, 0], [1, 2]], [[2, 0], [0, 1]]]
with self.session():
    for dtype in _TEST_TYPES:
        params_np = self._buildParams(data, dtype)
        params = constant_op.constant(params_np)
        indices_tf = constant_op.constant(indices)
        gather_t = array_ops.batch_gather(params, indices_tf)
        gather_val = self.evaluate(gather_t)
        expected_result = np.array([[[2, 0], [7, 5]], [[10, 8], [11, 15]]])
        np_val = self._buildParams(expected_result, dtype)
        self.assertAllEqual(np_val, gather_val)
        self.assertEqual(np_val.shape, gather_t.get_shape())
