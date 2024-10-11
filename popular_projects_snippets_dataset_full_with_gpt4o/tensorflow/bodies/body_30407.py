# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
inp = np.random.rand(4, 4).astype("i")
for k in range(4):
    with self.cached_session():
        a = constant_op.constant(inp, shape=[4, 4], dtype=dtypes.int32)
        slice_t = a[2, k:k]
        slice_val = self.evaluate(slice_t)
    self.assertAllEqual(slice_val, inp[2, k:k])
