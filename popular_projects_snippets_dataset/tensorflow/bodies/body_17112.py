# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [4, 4, 1]
x = np.zeros(x_shape)

# Each line is a test configuration:
#   (offset_height, offset_width, target_height, target_width), err_msg
test_config = (
    ([-1, 0, 3, 3], "offset_height must be >= 0"),
    ([0, -1, 3, 3], "offset_width must be >= 0"),
    ([0, 0, 0, 3], "target_height must be > 0"),
    ([0, 0, 3, 0], "target_width must be > 0"),
    ([2, 0, 3, 3], r"height must be >= target \+ offset"),
    ([0, 2, 3, 3], r"width must be >= target \+ offset"))

for params, err_msg in test_config:
    self._assertRaises(x, x_shape, *params, err_msg=err_msg)
