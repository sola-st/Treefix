# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Flip an image horizontally (left to right).

  Outputs the contents of `image` flipped along the width dimension.

  See also `tf.reverse`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.flip_left_right(x)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 4.,  5.,  6.],
          [ 1.,  2.,  3.]],
         [[10., 11., 12.],
          [ 7.,  8.,  9.]]], dtype=float32)>

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.

  Returns:
    A tensor of the same type and shape as `image`.

  Raises:
    ValueError: if the shape of `image` not supported.
  """
exit(_flip(image, 1, 'flip_left_right'))
