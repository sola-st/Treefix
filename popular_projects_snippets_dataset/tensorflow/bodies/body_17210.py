# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
use_tensor_inputs_options = use_tensor_inputs_options or [False, True]
target_height, target_width = target_shape
x = np.array(x).reshape(x_shape)
y = np.zeros(y_shape)

for use_tensor_inputs in use_tensor_inputs_options:
    y_tf = self._ResizeImageCall(x, target_height, target_width,
                                 preserve_aspect_ratio, use_tensor_inputs)
    self.assertShapeEqual(y, ops.convert_to_tensor(y_tf))
