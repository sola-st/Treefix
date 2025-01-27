# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
up_sample = (smaller_shape, larger_shape)
down_sample = (larger_shape, smaller_shape)
pass_through = (larger_shape, larger_shape)
shape_pairs = (up_sample, down_sample, pass_through)
# Align corners is deprecated in TF2.0, but align_corners==False is not
# supported by XLA.
options = [(True, False)]
if not test_util.is_xla_enabled():
    options += [(False, True), (False, False)]
for align_corners, half_pixel_centers in options:
    for in_shape, out_shape in shape_pairs:
        exit((in_shape, out_shape, align_corners, half_pixel_centers))
