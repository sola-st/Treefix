# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_np = np.array(original, dtype=original_dtype.as_numpy_dtype())
y_np = np.array(expected, dtype=output_dtype.as_numpy_dtype())

with self.cached_session():
    image = constant_op.constant(x_np)
    y = image_ops.convert_image_dtype(image, output_dtype)
    self.assertTrue(y.dtype == output_dtype)
    self.assertAllClose(y, y_np, atol=1e-5)
    if output_dtype in [
        dtypes.float32, dtypes.float64, dtypes.int32, dtypes.int64
    ]:
        y_saturate = image_ops.convert_image_dtype(
            image, output_dtype, saturate=True)
        self.assertTrue(y_saturate.dtype == output_dtype)
        self.assertAllClose(y_saturate, y_np, atol=1e-5)
