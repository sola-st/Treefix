# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Assert that we are working with a properly shaped image.

  Args:
    image: 3-D Tensor of shape [height, width, channels]
    require_static: If `True`, requires that all dimensions of `image` are known
      and non-zero.

  Raises:
    ValueError: if `image.shape` is not a 3-vector.

  Returns:
    An empty list, if `image` has fully defined dimensions. Otherwise, a list
    containing an assert op is returned.
  """
try:
    image_shape = image.get_shape().with_rank(3)
except ValueError:
    raise ValueError("'image' (shape %s) must be three-dimensional." %
                     image.shape)
if require_static and not image_shape.is_fully_defined():
    raise ValueError("'image' (shape %s) must be fully defined." % image_shape)
if any(x == 0 for x in image_shape):
    raise ValueError("all dims of 'image.shape' must be > 0: %s" % image_shape)
if not image_shape.is_fully_defined():
    exit([
        check_ops.assert_positive(
            array_ops.shape(image),
            ["all dims of 'image.shape' "
             'must be > 0.'])
    ])
else:
    exit([])
