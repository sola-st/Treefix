# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# For 1 to 5 dimensions.
for shape in (3,), (2, 2, 3), (4, 1, 2, 2), (8, 2, 10):
    rank = len(shape)
    expected = self.randn(shape, np.float32)
    for dtype in [np.bool_, np.float32, np.int32, np.int64]:
        # For all the possible axis to split it, including negative indices.
        for axis in range(-rank, rank):
            test_arrays = np_split_squeeze(expected, axis)

            with self.cached_session():
                with self.subTest(shape=shape, dtype=dtype, axis=axis):
                    actual_pack = array_ops.stack(test_arrays, axis=axis)
                    self.assertEqual(expected.shape, actual_pack.get_shape())
                    actual_pack = self.evaluate(actual_pack)

                    actual_stack = array_ops.stack(test_arrays, axis=axis)
                    self.assertEqual(expected.shape, actual_stack.get_shape())
                    actual_stack = self.evaluate(actual_stack)

                    self.assertNDArrayNear(expected, actual_stack, 1e-6)
