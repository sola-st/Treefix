# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
x_shape = [2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

delta = 0.25
y_data = [13, 0, 11, 226, 54, 221, 234, 8, 92, 1, 217, 255]
y_np = np.array(y_data, dtype=np.uint8).reshape(x_shape)

with self.session():
    x = array_ops.placeholder(x_np.dtype, shape=x_shape)
    flt_x = image_ops.convert_image_dtype(x, dtypes.float32)
    with self.test_scope():
        y = gen_image_ops.adjust_hue(flt_x, delta)
    y = image_ops.convert_image_dtype(y, x.dtype, saturate=True)
    y_tf = y.eval({x: x_np})
    self.assertAllEqual(y_tf, y_np)
