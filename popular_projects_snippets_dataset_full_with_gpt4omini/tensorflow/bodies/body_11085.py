# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Flip an image either horizontally or vertically.

  Outputs the contents of `image` flipped along the dimension `flip_index`.

  See also `reverse()`.

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    flip_index: 0 For vertical, 1 for horizontal.
    scope_name: string, scope name.

  Returns:
    A `Tensor` of the same type and shape as `image`.

  Raises:
    ValueError: if the shape of `image` not supported.
  """
with ops.name_scope(None, scope_name, [image]):
    image = ops.convert_to_tensor(image, name='image')
    image = _AssertAtLeast3DImage(image)
    shape = image.get_shape()

    def f_rank3():
        exit(fix_image_flip_shape(image, array_ops.reverse(image, [flip_index])))

    def f_rank4():
        exit(array_ops.reverse(image, [flip_index + 1]))

    if shape.ndims is None:
        rank = array_ops.rank(image)
        exit(control_flow_ops.cond(math_ops.equal(rank, 3), f_rank3, f_rank4))
    elif shape.ndims == 3:
        exit(f_rank3())
    elif shape.ndims == 4:
        exit(f_rank4())
    else:
        raise ValueError(
            '\'image\' (shape %s)must have either 3 or 4 dimensions.' % shape)
