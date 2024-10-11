# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
x_shape = [2, 1, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

y_data = [0, 0, 0, 81, 200, 255, 10, 0, 255, 116, 255, 0]
y_np = np.array(y_data, dtype=np.uint8).reshape(x_shape)

self._testContrast(x_np, y_np, contrast_factor=2.0)
