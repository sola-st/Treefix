# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
x_shape = [2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

saturation_factor = 2.0
y_data = [0, 5, 13, 0, 106, 226, 30, 0, 234, 89, 255, 0]
y_np = np.array(y_data, dtype=np.uint8).reshape(x_shape)

with self.session():
    x = array_ops.placeholder(x_np.dtype, shape=x_shape)
    y = self._adjust_saturation(x, saturation_factor)
    y_tf = y.eval({x: x_np})
    self.assertAllEqual(y_tf, y_np)
