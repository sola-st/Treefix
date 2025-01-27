# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
use_tensor_inputs_options = use_tensor_inputs_options or [False, True]
x = np.array(x).reshape(x_shape)

for use_tensor_inputs in use_tensor_inputs_options:
    with self.assertRaisesRegex(
        (ValueError, errors.InvalidArgumentError), err_msg):
        self._ResizeImageWithPad(x, target_height, target_width,
                                 use_tensor_inputs)
