# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [1, 2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.float64).reshape(x_shape) / 255.

y_data = [
    -45.25, -90.75, -92.5, 62.75, 169.25, 333.5, 28.75, -84.75, 349.5,
    134.75, 409.25, -116.5
]
y_np = np.array(y_data, dtype=np.float64).reshape(x_shape) / 255.

self._testContrast(x_np, y_np, contrast_factor=2.0)
