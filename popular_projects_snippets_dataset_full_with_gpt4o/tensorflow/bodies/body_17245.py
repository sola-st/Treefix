# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Input image has 0-length dimension(s).
target_height, target_width = [1, 1]
x = []

for x_shape in ([0, 2, 2], [2, 0, 2], [2, 2, 0]):
    self._assertRaises(
        x,
        x_shape,
        target_height,
        target_width,
        "inner 3 dims of 'image.shape' must be > 0",
        use_tensor_inputs_options=[False])

    # The original error message does not contain back slashes. However, they
    # are added by either the assert op or the runtime. If this behavior
    # changes in the future, the match string will also needs to be changed.
    self._assertRaises(
        x,
        x_shape,
        target_height,
        target_width,
        "inner 3 dims of \\'image.shape\\' must be > 0",
        use_tensor_inputs_options=[True])
