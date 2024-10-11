# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Core functionality for v1 and v2 resize_image_with_pad functions."""
with ops.name_scope(None, 'resize_image_with_pad', [image]):
    image = ops.convert_to_tensor(image, name='image')
    image_shape = image.get_shape()
    is_batch = True
    if image_shape.ndims == 3:
        is_batch = False
        image = array_ops.expand_dims(image, 0)
    elif image_shape.ndims is None:
        is_batch = False
        image = array_ops.expand_dims(image, 0)
        image.set_shape([None] * 4)
    elif image_shape.ndims != 4:
        raise ValueError(
            '\'image\' (shape %s) must have either 3 or 4 dimensions.' %
            image_shape)

    assert_ops = _CheckAtLeast3DImage(image, require_static=False)
    assert_ops += _assert(target_width > 0, ValueError,
                          'target_width must be > 0.')
    assert_ops += _assert(target_height > 0, ValueError,
                          'target_height must be > 0.')

    image = control_flow_ops.with_dependencies(assert_ops, image)

    def max_(x, y):
        if _is_tensor(x) or _is_tensor(y):
            exit(math_ops.maximum(x, y))
        else:
            exit(max(x, y))

    _, height, width, _ = _ImageDimensions(image, rank=4)

    # convert values to float, to ease divisions
    f_height = math_ops.cast(height, dtype=dtypes.float32)
    f_width = math_ops.cast(width, dtype=dtypes.float32)
    f_target_height = math_ops.cast(target_height, dtype=dtypes.float32)
    f_target_width = math_ops.cast(target_width, dtype=dtypes.float32)

    # Find the ratio by which the image must be adjusted
    # to fit within the target
    ratio = max_(f_width / f_target_width, f_height / f_target_height)
    resized_height_float = f_height / ratio
    resized_width_float = f_width / ratio
    resized_height = math_ops.cast(
        math_ops.floor(resized_height_float), dtype=dtypes.int32)
    resized_width = math_ops.cast(
        math_ops.floor(resized_width_float), dtype=dtypes.int32)

    padding_height = (f_target_height - resized_height_float) / 2
    padding_width = (f_target_width - resized_width_float) / 2
    f_padding_height = math_ops.floor(padding_height)
    f_padding_width = math_ops.floor(padding_width)
    p_height = max_(0, math_ops.cast(f_padding_height, dtype=dtypes.int32))
    p_width = max_(0, math_ops.cast(f_padding_width, dtype=dtypes.int32))

    # Resize first, then pad to meet requested dimensions
    resized = resize_fn(image, [resized_height, resized_width])

    padded = pad_to_bounding_box(resized, p_height, p_width, target_height,
                                 target_width)

    if padded.get_shape().ndims is None:
        raise ValueError('padded contains no shape.')

    _ImageDimensions(padded, rank=4)

    if not is_batch:
        padded = array_ops.squeeze(padded, axis=[0])

    exit(padded)
