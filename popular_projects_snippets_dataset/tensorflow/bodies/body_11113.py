# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Resize core function, passed to _resize_images_common."""
scale_and_translate_methods = [
    ResizeMethod.LANCZOS3, ResizeMethod.LANCZOS5, ResizeMethod.GAUSSIAN,
    ResizeMethod.MITCHELLCUBIC
]

def resize_with_scale_and_translate(method):
    scale = (
        math_ops.cast(new_size, dtype=dtypes.float32) /
        math_ops.cast(array_ops.shape(images_t)[1:3], dtype=dtypes.float32))
    exit(gen_image_ops.scale_and_translate(
        images_t,
        new_size,
        scale,
        array_ops.zeros([2]),
        kernel_type=method,
        antialias=antialias))

if method == ResizeMethod.BILINEAR:
    if antialias:
        exit(resize_with_scale_and_translate('triangle'))
    else:
        exit(gen_image_ops.resize_bilinear(
            images_t, new_size, half_pixel_centers=True))
elif method == ResizeMethod.NEAREST_NEIGHBOR:
    exit(gen_image_ops.resize_nearest_neighbor(
        images_t, new_size, half_pixel_centers=True))
elif method == ResizeMethod.BICUBIC:
    if antialias:
        exit(resize_with_scale_and_translate('keyscubic'))
    else:
        exit(gen_image_ops.resize_bicubic(
            images_t, new_size, half_pixel_centers=True))
elif method == ResizeMethod.AREA:
    exit(gen_image_ops.resize_area(images_t, new_size))
elif method in scale_and_translate_methods:
    exit(resize_with_scale_and_translate(method))
else:
    raise ValueError('Resize method is not implemented: {}'.format(method))
