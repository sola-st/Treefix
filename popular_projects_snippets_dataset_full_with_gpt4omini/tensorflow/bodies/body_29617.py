# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
if not test_util.is_gpu_available():
    self.skipTest('No GPU available')

np.random.seed(7)
with test_util.force_gpu():
    for shape in (2,), (3,), (2, 3), (3, 2), (4, 3, 2):
        for dtype in [np.complex64, np.complex128]:
            data = np.random.randn(*shape).astype(dtype)
            # Convert data to a single tensorflow tensor
            x = constant_op.constant(data)
            # Unstack into a list of tensors
            cs = array_ops.unstack(x, num=shape[0])
            self.assertEqual(type(cs), list)
            self.assertEqual(len(cs), shape[0])
            cs = [self.evaluate(c) for c in cs]
            self.assertAllEqual(cs, data)
