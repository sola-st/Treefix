# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with test_util.use_gpu():
    for dtype in [
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.int32,
        np.int64,
        np.bool_,
        np.float16,
        np.float32,
        np.float64,
        np.complex64,
        np.complex128,
        dtypes.bfloat16.as_numpy_dtype,
    ]:
        inp = np.random.rand(4, 4).astype(dtype)
        a = constant_op.constant(
            [float(x) for x in inp.ravel(order="C")],
            shape=[4, 4],
            dtype=dtypes.float32)
        slice_t = array_ops.slice(a, [0, 0], [2, 2])
        slice2_t = a[:2, :2]
        slice_val, slice2_val = self.evaluate([slice_t, slice2_t])
        self.assertAllEqual(slice_val, np.array(inp[:2, :2], dtype=np.float32))
        self.assertAllEqual(slice2_val, np.array(inp[:2, :2], dtype=np.float32))
        self.assertEqual(slice_val.shape, slice_t.get_shape())
        self.assertEqual(slice2_val.shape, slice2_t.get_shape())
