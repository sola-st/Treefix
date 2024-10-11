# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.float32).reshape(x_shape) / 255.

y_data = [10, 15, 23, 64, 145, 236, 47, 18, 244, 100, 265, 11]
y_np = np.array(y_data, dtype=np.float32).reshape(x_shape) / 255.

self._testBrightness(x_np, y_np, delta=10. / 255.)
