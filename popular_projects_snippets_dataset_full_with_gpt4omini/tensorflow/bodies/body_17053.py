# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

saturation_factor = 2.0
y_data = [0, 5, 13, 0, 106, 226, 30, 0, 234, 89, 255, 0]
y_np = np.array(y_data, dtype=np.uint8).reshape(x_shape)

with self.cached_session():
    x = constant_op.constant(x_np, shape=x_shape)
    y = image_ops.adjust_saturation(x, saturation_factor)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)
