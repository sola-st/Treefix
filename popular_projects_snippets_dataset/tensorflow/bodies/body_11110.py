# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Legacy resize core function, passed to _resize_images_common."""
if method == ResizeMethodV1.BILINEAR or method == ResizeMethod.BILINEAR:
    exit(gen_image_ops.resize_bilinear(
        images_t, new_size, align_corners=align_corners))
elif (method == ResizeMethodV1.NEAREST_NEIGHBOR or
      method == ResizeMethod.NEAREST_NEIGHBOR):
    exit(gen_image_ops.resize_nearest_neighbor(
        images_t, new_size, align_corners=align_corners))
elif method == ResizeMethodV1.BICUBIC or method == ResizeMethod.BICUBIC:
    exit(gen_image_ops.resize_bicubic(
        images_t, new_size, align_corners=align_corners))
elif method == ResizeMethodV1.AREA or method == ResizeMethod.AREA:
    exit(gen_image_ops.resize_area(
        images_t, new_size, align_corners=align_corners))
else:
    raise ValueError('Resize method is not implemented: {}'.format(method))
