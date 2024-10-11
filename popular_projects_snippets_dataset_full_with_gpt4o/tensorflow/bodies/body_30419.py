# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
for _ in range(10):
    with self.cached_session():
        inp = np.random.rand(4, 4).astype("f")
        a = constant_op.constant(inp, shape=[4, 4], dtype=dtypes.float32)

        x, y = np.random.randint(0, 3, size=2).tolist()
        slice_t = a[x, 0:y]
        slice_val = self.evaluate(slice_t)
    self.assertAllEqual(slice_val, inp[x, 0:y])
