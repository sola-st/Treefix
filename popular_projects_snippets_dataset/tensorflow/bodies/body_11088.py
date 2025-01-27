# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Rotate image(s) by 90 degrees.


  For example:

  >>> a=tf.constant([[[1],[2]],
  ...                [[3],[4]]])
  >>> # rotating `a` counter clockwise by 90 degrees
  >>> a_rot=tf.image.rot90(a)
  >>> print(a_rot[...,0].numpy())
  [[2 4]
   [1 3]]
  >>> # rotating `a` counter clockwise by 270 degrees
  >>> a_rot=tf.image.rot90(a, k=3)
  >>> print(a_rot[...,0].numpy())
  [[3 1]
   [4 2]]
  >>> # rotating `a` clockwise by 180 degrees
  >>> a_rot=tf.image.rot90(a, k=-2)
  >>> print(a_rot[...,0].numpy())
  [[4 3]
   [2 1]]

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    k: A scalar integer tensor. The number of times the image(s) are rotated by
      90 degrees.
    name: A name for this operation (optional).

  Returns:
    A rotated tensor of the same type and shape as `image`.

  Raises:
    ValueError: if the shape of `image` not supported.
  """
with ops.name_scope(name, 'rot90', [image, k]) as scope:
    image = ops.convert_to_tensor(image, name='image')
    image = _AssertAtLeast3DImage(image)
    k = ops.convert_to_tensor(k, dtype=dtypes.int32, name='k')
    k.get_shape().assert_has_rank(0)
    k = math_ops.mod(k, 4)

    shape = image.get_shape()
    if shape.ndims is None:
        rank = array_ops.rank(image)

        def f_rank3():
            exit(_rot90_3D(image, k, scope))

        def f_rank4():
            exit(_rot90_4D(image, k, scope))

        exit(control_flow_ops.cond(math_ops.equal(rank, 3), f_rank3, f_rank4))
    elif shape.ndims == 3:
        exit(_rot90_3D(image, k, scope))
    elif shape.ndims == 4:
        exit(_rot90_4D(image, k, scope))
    else:
        raise ValueError(
            '\'image\' (shape %s) must have either 3 or 4 dimensions.' % shape)
