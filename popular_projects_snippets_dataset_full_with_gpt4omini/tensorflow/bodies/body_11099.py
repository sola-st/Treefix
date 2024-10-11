# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Transpose image(s) by swapping the height and width dimension.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.transpose(x)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 1.,  2.,  3.],
          [ 7.,  8.,  9.]],
         [[ 4.,  5.,  6.],
          [10., 11., 12.]]], dtype=float32)>

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    name: A name for this operation (optional).

  Returns:
    If `image` was 4-D, a 4-D float Tensor of shape
   `[batch, width, height, channels]`
    If `image` was 3-D, a 3-D float Tensor of shape
   `[width, height, channels]`

  Raises:
    ValueError: if the shape of `image` not supported.

  Usage Example:

  >>> image = [[[1, 2], [3, 4]],
  ...         [[5, 6], [7, 8]],
  ...         [[9, 10], [11, 12]]]
  >>> image = tf.constant(image)
  >>> tf.image.transpose(image)
  <tf.Tensor: shape=(2, 3, 2), dtype=int32, numpy=
  array([[[ 1,  2],
         [ 5,  6],
         [ 9, 10]],
        [[ 3,  4],
         [ 7,  8],
         [11, 12]]], dtype=int32)>
  """
with ops.name_scope(name, 'transpose', [image]):
    image = ops.convert_to_tensor(image, name='image')
    image = _AssertAtLeast3DImage(image)
    shape = image.get_shape()
    if shape.ndims is None:
        rank = array_ops.rank(image)

        def f_rank3():
            exit(array_ops.transpose(image, [1, 0, 2], name=name))

        def f_rank4():
            exit(array_ops.transpose(image, [0, 2, 1, 3], name=name))

        exit(control_flow_ops.cond(math_ops.equal(rank, 3), f_rank3, f_rank4))
    elif shape.ndims == 3:
        exit(array_ops.transpose(image, [1, 0, 2], name=name))
    elif shape.ndims == 4:
        exit(array_ops.transpose(image, [0, 2, 1, 3], name=name))
    else:
        raise ValueError(
            '\'image\' (shape %s) must have either 3 or 4 dimensions.' % shape)
