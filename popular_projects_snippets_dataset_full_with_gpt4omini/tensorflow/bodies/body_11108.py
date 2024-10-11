# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Crops and/or pads an image to a target width and height.

  Resizes an image to a target width and height by either centrally
  cropping the image or padding it evenly with zeros.

  If `width` or `height` is greater than the specified `target_width` or
  `target_height` respectively, this op centrally crops along that dimension.

  For example:

  >>> image = np.arange(75).reshape(5, 5, 3)  # create 3-D image input
  >>> image[:,:,0]  # print first channel just for demo purposes
  array([[ 0,  3,  6,  9, 12],
         [15, 18, 21, 24, 27],
         [30, 33, 36, 39, 42],
         [45, 48, 51, 54, 57],
         [60, 63, 66, 69, 72]])
  >>> image = tf.image.resize_with_crop_or_pad(image, 3, 3)  # crop
  >>> # print first channel for demo purposes; centrally cropped output
  >>> image[:,:,0]
  <tf.Tensor: shape=(3, 3), dtype=int64, numpy=
  array([[18, 21, 24],
         [33, 36, 39],
         [48, 51, 54]])>

  If `width` or `height` is smaller than the specified `target_width` or
  `target_height` respectively, this op centrally pads with 0 along that
  dimension.

  For example:

  >>> image = np.arange(1, 28).reshape(3, 3, 3)  # create 3-D image input
  >>> image[:,:,0]  # print first channel just for demo purposes
  array([[ 1,  4,  7],
         [10, 13, 16],
         [19, 22, 25]])
  >>> image = tf.image.resize_with_crop_or_pad(image, 5, 5)  # pad
  >>> # print first channel for demo purposes; we should see 0 paddings
  >>> image[:,:,0]
  <tf.Tensor: shape=(5, 5), dtype=int64, numpy=
  array([[ 0,  0,  0,  0,  0],
         [ 0,  1,  4,  7,  0],
         [ 0, 10, 13, 16,  0],
         [ 0, 19, 22, 25,  0],
         [ 0,  0,  0,  0,  0]])>

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    target_height: Target height.
    target_width: Target width.

  Raises:
    ValueError: if `target_height` or `target_width` are zero or negative.

  Returns:
    Cropped and/or padded image.
    If `images` was 4-D, a 4-D float Tensor of shape
    `[batch, new_height, new_width, channels]`.
    If `images` was 3-D, a 3-D float Tensor of shape
    `[new_height, new_width, channels]`.
  """
with ops.name_scope(None, 'resize_image_with_crop_or_pad', [image]):
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
    # `crop_to_bounding_box` and `pad_to_bounding_box` have their own checks.
    # Make sure our checks come first, so that error messages are clearer.
    if _is_tensor(target_height):
        target_height = control_flow_ops.with_dependencies(
            assert_ops, target_height)
    if _is_tensor(target_width):
        target_width = control_flow_ops.with_dependencies(assert_ops,
                                                          target_width)

    def max_(x, y):
        if _is_tensor(x) or _is_tensor(y):
            exit(math_ops.maximum(x, y))
        else:
            exit(max(x, y))

    def min_(x, y):
        if _is_tensor(x) or _is_tensor(y):
            exit(math_ops.minimum(x, y))
        else:
            exit(min(x, y))

    def equal_(x, y):
        if _is_tensor(x) or _is_tensor(y):
            exit(math_ops.equal(x, y))
        else:
            exit(x == y)

    _, height, width, _ = _ImageDimensions(image, rank=4)
    width_diff = target_width - width
    offset_crop_width = max_(-width_diff // 2, 0)
    offset_pad_width = max_(width_diff // 2, 0)

    height_diff = target_height - height
    offset_crop_height = max_(-height_diff // 2, 0)
    offset_pad_height = max_(height_diff // 2, 0)

    # Maybe crop if needed.
    cropped = crop_to_bounding_box(image, offset_crop_height, offset_crop_width,
                                   min_(target_height, height),
                                   min_(target_width, width))

    # Maybe pad if needed.
    resized = pad_to_bounding_box(cropped, offset_pad_height, offset_pad_width,
                                  target_height, target_width)

    # In theory all the checks below are redundant.
    if resized.get_shape().ndims is None:
        raise ValueError('resized contains no shape.')

    _, resized_height, resized_width, _ = _ImageDimensions(resized, rank=4)

    assert_ops = []
    assert_ops += _assert(
        equal_(resized_height, target_height), ValueError,
        'resized height is not correct.')
    assert_ops += _assert(
        equal_(resized_width, target_width), ValueError,
        'resized width is not correct.')

    resized = control_flow_ops.with_dependencies(assert_ops, resized)

    if not is_batch:
        resized = array_ops.squeeze(resized, axis=[0])

    exit(resized)
