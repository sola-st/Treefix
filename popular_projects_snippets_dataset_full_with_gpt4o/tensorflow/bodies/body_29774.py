# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
types_to_test = {
    "bool": (dtypes.bool, bool),
    "bfloat16": (dtypes.bfloat16, float),
    "float16": (dtypes.float16, float),
    "float32": (dtypes.float32, float),
    "float64": (dtypes.float64, float),
    "complex64": (dtypes.complex64, complex),
    "complex128": (dtypes.complex128, complex),
    "uint8": (dtypes.uint8, int),
    "int8": (dtypes.int8, int),
    "int16": (dtypes.int16, int),
    "int32": (dtypes.int32, int),
    "int64": (dtypes.int64, int),
    "uint32": (dtypes.uint32, int),
    "uint64": (dtypes.uint64, int),
    bytes: (dtypes.string, bytes)
}
for dtype_np, (dtype_tf, cast) in types_to_test.items():
    with self.cached_session():
        inp = np.random.rand(4, 1).astype(dtype_np)
        a = constant_op.constant(
            [cast(x) for x in inp.ravel(order="C")],
            shape=[4, 1],
            dtype=dtype_tf)
        tiled = array_ops.tile(a, [1, 4])
        result = self.evaluate(tiled)
    self.assertEqual(result.shape, (4, 4))
    self.assertEqual([4, 4], tiled.get_shape())
    self.assertAllEqual(result, np.tile(inp, (1, 4)))
