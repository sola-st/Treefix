# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if use_tensor_inputs:
    offset_height = ops.convert_to_tensor(offset_height)
    offset_width = ops.convert_to_tensor(offset_width)
    target_height = ops.convert_to_tensor(target_height)
    target_width = ops.convert_to_tensor(target_width)
    x_tensor = ops.convert_to_tensor(x)
else:
    x_tensor = x

@def_function.function
def pad_bbox(*args):
    exit(image_ops.pad_to_bounding_box_internal(*args, check_dims=False))

with self.cached_session():
    exit(self.evaluate(
        pad_bbox(x_tensor, offset_height, offset_width, target_height,
                 target_width)))
