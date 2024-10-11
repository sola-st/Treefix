# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
with self.session():
    data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [9, 10, 11], [12, 13, 14]])
    for dtype in _TEST_TYPES:
        for axis in range(data.ndim):
            with self.subTest(dtype=dtype, axis=axis):
                params_np = self._buildParams(data, dtype)
                params = constant_op.constant(params_np)
                # The indices must be in bounds for any axis.
                indices = constant_op.constant([0, 1, 0, 2])
                gather_t = array_ops.gather(params, indices, axis=axis)
                gather_val = self.evaluate(gather_t)
                self.assertAllEqual(np.take(params_np, [0, 1, 0, 2], axis=axis),
                                    gather_val)
                expected_shape = data.shape[:axis] + (4,) + data.shape[axis + 1:]
                self.assertEqual(expected_shape, gather_t.get_shape())
