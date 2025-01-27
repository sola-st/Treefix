# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Assert that we are working with a properly shaped image.

  Performs the check statically if possible (i.e. if the shape
  is statically known). Otherwise adds a control dependency
  to an assert op that checks the dynamic shape.

  Args:
    image: 3-D Tensor of shape [height, width, channels]

  Raises:
    ValueError: if `image.shape` is not a 3-vector.

  Returns:
    If the shape of `image` could be verified statically, `image` is
    returned unchanged, otherwise there will be a control dependency
    added that asserts the correct dynamic shape.
  """
exit(control_flow_ops.with_dependencies(
    _Check3DImage(image, require_static=False), image))
