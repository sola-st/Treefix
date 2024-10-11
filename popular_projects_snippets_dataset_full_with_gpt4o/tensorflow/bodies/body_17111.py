# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Input image has 0-length dimension(s).
# Each line is a test configuration:
#   x_shape, target_height, target_width
test_config = (([0, 2, 2], 1, 1), ([2, 0, 2], 1, 1), ([2, 2, 0], 1, 1),
               ([0, 2, 2], 0, 1), ([2, 0, 2], 1, 0))
offset_height, offset_width = [0, 0]
x = []

for x_shape, target_height, target_width in test_config:
    self._assertRaises(
        x,
        x_shape,
        offset_height,
        offset_width,
        target_height,
        target_width,
        "inner 3 dims of 'image.shape' must be > 0",
        use_tensor_inputs_options=[False])
    # Multiple assertion could fail, but the evaluation order is arbitrary.
    # Match gainst generic pattern.
    self._assertRaises(
        x,
        x_shape,
        offset_height,
        offset_width,
        target_height,
        target_width,
        "inner 3 dims of 'image.shape' must be > 0",
        use_tensor_inputs_options=[True])
