# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
for dtype in [
    dtypes.float32, dtypes.float64, dtypes.int32, dtypes.int64, dtypes.bool,
    dtypes.uint8, dtypes.bfloat16
]:
    with test_util.use_gpu():
        test_shapes = [(), (1,), (2, 3), (0, 2), (2, 3, 5), (2, 0, 5)]
        for shape in test_shapes:
            val = self.evaluate(inplace_ops.empty(shape, dtype))
            self.assertEqual(val.shape, shape)
            self.assertEqual(val.dtype, dtype.as_numpy_dtype)
            val = self.evaluate(inplace_ops.empty(shape, dtype, init=True))
            self.assertEqual(val.shape, shape)
            self.assertEqual(val.dtype, dtype.as_numpy_dtype)
            self.assertAllEqual(val, np.zeros(shape, dtype.as_numpy_dtype))
            val = self.evaluate(
                inplace_ops.empty_like(array_ops.zeros(shape, dtype)))
            self.assertEqual(val.shape, shape)
            self.assertEqual(val.dtype, dtype.as_numpy_dtype)
            val = self.evaluate(inplace_ops.empty_like(
                array_ops.zeros(shape, dtype), init=True))
            self.assertEqual(val.shape, shape)
            self.assertEqual(val.dtype, dtype.as_numpy_dtype)
            self.assertAllEqual(val, np.zeros(shape, dtype.as_numpy_dtype))

with test_util.use_gpu():
    val = self.evaluate(inplace_ops.empty((1, 2), dtypes.string, init=True))
    self.assertEqual(val.tolist(), [[b"", b""]])

    val = self.evaluate(inplace_ops.empty((1, 2), dtypes.string, init=False))
    self.assertEqual(val.tolist(), [[b"", b""]])
