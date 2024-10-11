# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
with self.cached_session():
    data = np.array([0, 1, 2, 3, 7, 5])
    for dtype in _TEST_TYPES:
        for indices in 4, [1, 2, 2, 4, 5]:
            with self.subTest(dtype=dtype, indices=indices):
                params_np = self._buildParams(data, dtype)
                params = constant_op.constant(params_np)
                indices_tf = constant_op.constant(indices)
                gather_t = array_ops.gather(params, indices_tf)
                gather_val = self.evaluate(gather_t)
                np_val = params_np[indices]
                self.assertAllEqual(np_val, gather_val)
                self.assertEqual(np_val.shape, gather_t.get_shape())
