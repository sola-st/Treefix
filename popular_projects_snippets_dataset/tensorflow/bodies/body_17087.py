# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [1, 2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

y_data = [22, 52, 65, 49, 118, 172, 41, 54, 176, 67, 178, 59]
y_np = np.array(y_data, dtype=np.uint8).reshape(x_shape)

self._testContrast(x_np, y_np, contrast_factor=0.5)
