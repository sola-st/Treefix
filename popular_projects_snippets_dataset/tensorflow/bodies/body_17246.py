# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [4, 4, 1]
x = np.zeros(x_shape)

# target_height <= 0
target_height, target_width = [0, 5]
self._assertRaises(x, x_shape, target_height, target_width,
                   "target_height must be > 0")

# target_width <= 0
target_height, target_width = [5, 0]
self._assertRaises(x, x_shape, target_height, target_width,
                   "target_width must be > 0")
