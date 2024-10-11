# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if use_tensor_inputs:
    target_height = ops.convert_to_tensor(target_height)
    target_width = ops.convert_to_tensor(target_width)
    x_tensor = ops.convert_to_tensor(x)
else:
    x_tensor = x

with self.cached_session():
    exit(self.evaluate(
        image_ops.resize_image_with_pad_v2(x_tensor, target_height,
                                           target_width)))
