# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
use_tensor_inputs_options = use_tensor_inputs_options or [False, True]
target_height, target_width, _ = y_shape
x = np.array(x).reshape(x_shape)
y = np.array(y).reshape(y_shape)

for use_tensor_inputs in use_tensor_inputs_options:
    y_tf = self._CropToBoundingBox(x, offset_height, offset_width,
                                   target_height, target_width,
                                   use_tensor_inputs)
    self.assertAllClose(y, y_tf)
