# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Flip an image vertically (upside down).

  Outputs the contents of `image` flipped along the height dimension.

  See also `reverse()`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.flip_up_down(x)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 7.,  8.,  9.],
          [10., 11., 12.]],
         [[ 1.,  2.,  3.],
          [ 4.,  5.,  6.]]], dtype=float32)>

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.

  Returns:
    A `Tensor` of the same type and shape as `image`.

  Raises:
    ValueError: if the shape of `image` not supported.
  """
exit(_flip(image, 0, 'flip_up_down'))
