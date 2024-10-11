# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Assert that we are working with properly shaped grayscale image.

  Args:
    image: >= 2-D Tensor of size [*, 1]
    require_static: Boolean, whether static shape is required.

  Raises:
    ValueError: if image.shape is not a [>= 2] vector or if
              last dimension is not size 1.

  Returns:
    An empty list, if `image` has fully defined dimensions. Otherwise, a list
    containing an assert op is returned.
  """
try:
    if image.get_shape().ndims is None:
        image_shape = image.get_shape().with_rank(2)
    else:
        image_shape = image.get_shape().with_rank_at_least(2)
except ValueError:
    raise ValueError('A grayscale image (shape %s) must be at least '
                     'two-dimensional.' % image.shape)
if require_static and not image_shape.is_fully_defined():
    raise ValueError('\'image\' must be fully defined.')
if image_shape.is_fully_defined():
    if image_shape[-1] != 1:
        raise ValueError('Last dimension of a grayscale image should be size 1.')
if not image_shape.is_fully_defined():
    exit([
        check_ops.assert_equal(
            array_ops.shape(image)[-1],
            1,
            message='Last dimension of a grayscale image should be size 1.'),
        check_ops.assert_greater_equal(
            array_ops.rank(image),
            3,
            message='A grayscale image must be at least two-dimensional.')
    ])
else:
    exit([])
