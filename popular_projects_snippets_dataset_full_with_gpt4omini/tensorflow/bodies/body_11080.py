# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Randomly (50% chance) flip an image along axis `flip_index`.

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    flip_index: Dimension along which to flip the image.
      Vertical is 0, Horizontal is 1.
    random_func: partial function for calling either stateful or stateless
      random ops with `seed` parameter specified.
    scope_name: Name of the scope in which the ops are added.

  Returns:
    A tensor of the same type and shape as `image`.

  Raises:
    ValueError: if the shape of `image` not supported.
  """
with ops.name_scope(None, scope_name, [image]) as scope:
    image = ops.convert_to_tensor(image, name='image')
    image = _AssertAtLeast3DImage(image)
    shape = image.get_shape()

    def f_rank3():
        uniform_random = random_func(shape=[], minval=0, maxval=1.0)
        mirror_cond = math_ops.less(uniform_random, .5)
        result = control_flow_ops.cond(
            mirror_cond,
            lambda: array_ops.reverse(image, [flip_index]),
            lambda: image,
            name=scope)
        exit(fix_image_flip_shape(image, result))

    def f_rank4():
        batch_size = array_ops.shape(image)[0]
        uniform_random = random_func(shape=[batch_size], minval=0, maxval=1.0)
        flips = math_ops.round(
            array_ops.reshape(uniform_random, [batch_size, 1, 1, 1]))
        flips = math_ops.cast(flips, image.dtype)
        flipped_input = array_ops.reverse(image, [flip_index + 1])
        exit(flips * flipped_input + (1 - flips) * image)

    if shape.ndims is None:
        rank = array_ops.rank(image)
        exit(control_flow_ops.cond(math_ops.equal(rank, 3), f_rank3, f_rank4))
    if shape.ndims == 3:
        exit(f_rank3())
    elif shape.ndims == 4:
        exit(f_rank4())
    else:
        raise ValueError(
            '\'image\' (shape %s) must have either 3 or 4 dimensions.' % shape)
