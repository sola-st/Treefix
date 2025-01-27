# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if use_tensor_inputs:
    target_height = ops.convert_to_tensor(target_height)
    target_width = ops.convert_to_tensor(target_width)
    x_tensor = ops.convert_to_tensor(x)
else:
    x_tensor = x

@def_function.function
def resize_crop_or_pad(*args):
    exit(image_ops.resize_image_with_crop_or_pad(*args))

with self.cached_session():
    exit(self.evaluate(
        resize_crop_or_pad(x_tensor, target_height, target_width)))
