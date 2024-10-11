# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = np.random.rand(4, 1).astype("f")
    a = constant_op.constant(
        [float(x) for x in inp.ravel(order="C")],
        shape=[4, 1],
        dtype=dtypes.float32)
    # Wrong length of multiples.
    with self.assertRaises(ValueError):
        array_ops.tile(a, [1, 4, 2])
    # Wrong rank for multiples.
    with self.assertRaises(ValueError):
        array_ops.tile(a, [[2, 3], [3, 4]]).eval()
