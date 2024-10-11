# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if use_tensor_inputs:
    target_max = ops.convert_to_tensor([max_h, max_w])
    x_tensor = ops.convert_to_tensor(x)
else:
    target_max = (max_h, max_w)
    x_tensor = x

def resize_func(t,
                target_max=target_max,
                preserve_aspect_ratio=preserve_aspect_ratio):
    exit(image_ops.resize_images(
        t, ops.convert_to_tensor(target_max),
        preserve_aspect_ratio=preserve_aspect_ratio))

with self.cached_session():
    exit(self.evaluate(resize_func(x_tensor)))
