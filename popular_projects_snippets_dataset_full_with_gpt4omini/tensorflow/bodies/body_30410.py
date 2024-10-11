# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
for _ in range(10):
    with self.cached_session():
        inp = np.random.rand(4, 4, 4, 4).astype("f")
        a = constant_op.constant(inp, shape=[4, 4, 4, 4], dtype=dtypes.float32)

        slice_explicit_t = array_ops.slice(a, [0, 0, 0, 0], [-1, -1, -1, -1])
        slice_implicit_t = a[:, :, :, :]

        self.assertAllEqual(inp, self.evaluate(slice_explicit_t))
        self.assertAllEqual(inp, self.evaluate(slice_implicit_t))
        self.assertEqual(inp.shape, slice_explicit_t.get_shape())
        self.assertEqual(inp.shape, slice_implicit_t.get_shape())
