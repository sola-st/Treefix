# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Input image is not 3D
x = [0] * 15
offset_height, offset_width = [0, 0]
target_height, target_width = [2, 2]

for x_shape in ([3, 5], [1, 3, 5, 1, 1]):
    self._assertRaises(x, x_shape, offset_height, offset_width, target_height,
                       target_width,
                       "must have either 3 or 4 dimensions.")
