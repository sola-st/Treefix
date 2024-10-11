# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
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
