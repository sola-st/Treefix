# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
inp = np.random.rand(4, 10, 10, 4).astype("f")
a = constant_op.constant(inp, dtype=dtypes.float32)

x = np.random.randint(0, 9)
z = np.random.randint(0, 9)
if z > 0:
    y = np.random.randint(0, z)
else:
    y = 0
slice_t = a[:, x, y:z, :]
self.assertAllEqual(slice_t, inp[:, x, y:z, :])
