# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
with self.session():
    x = array_ops.placeholder(x_np.dtype, shape=x_np.shape)
    flt_x = image_ops.convert_image_dtype(x, dtypes.float32)
    with self.test_scope():
        y = image_ops.adjust_contrast(flt_x, contrast_factor)
    y = image_ops.convert_image_dtype(y, x.dtype, saturate=True)
    y_tf = y.eval({x: x_np})
    self.assertAllClose(y_tf, y_np, 1e-6)
