# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
if not test_util.is_gpu_available():
    self.skipTest('No GPU available')

np.random.seed(7)
with test_util.force_gpu():
    for shape in (2,), (3,), (2, 3), (3, 2), (4, 3, 2):
        rank = len(shape)
        for axis in range(-rank, rank):
            for dtype in [
                np.bool_, np.float16, np.float32, np.float64, np.uint8, np.int32,
                np.int64
            ]:
                data = self.randn(shape, dtype)
                # Convert data to a single tensorflow tensor
                x = constant_op.constant(data)
                # Unstack into a list of tensors
                ref = self.unstackReference(data, axis)
                cs = array_ops.unstack(x, axis=axis)
                self.assertEqual(type(cs), list)
                self.assertEqual(len(cs), shape[axis])
                for k, c in enumerate(cs):
                    # Give error with loop context
                    with self.subTest(shape=shape, k=k, axis=axis, dtype=dtype):
                        self.assertAllEqual(ref[k], self.evaluate(c))
