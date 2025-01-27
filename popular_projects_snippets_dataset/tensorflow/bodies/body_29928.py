# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
np.random.seed(7)
for shape in (2,), (3,), (2, 3), (3, 2), (8, 2, 10):
    rank = len(shape)
    for axis in range(-rank, rank):
        for dtype in [np.bool_, np.float32, np.int32, np.int64]:
            data = self.randn(shape, dtype)
            xs = np_split_squeeze(data, axis)
            # Stack back into a single tensorflow tensor
            with self.subTest(shape=shape, axis=axis, dtype=dtype):
                c = array_ops.stack(xs, axis=axis)
                self.assertAllEqual(c, data)
