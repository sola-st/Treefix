# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    # Random dims of given rank
    input_shape = np.random.randint(1, 4, size=rank)
    inp = np.random.rand(*input_shape).astype("f")
    a = constant_op.constant(
        [float(x) for x in inp.ravel(order="C")],
        shape=input_shape,
        dtype=dtypes.float32)
    multiples = np.random.randint(1, 4, size=rank).astype(np.int32)
    tiled = array_ops.tile(a, multiples)
    result = self.evaluate(tiled)
self.assertTrue((np.array(multiples) * np.array(inp.shape) == np.array(
    result.shape)).all())
self.assertAllEqual(result, np.tile(inp, tuple(multiples)))
self.assertShapeEqual(result, tiled)
