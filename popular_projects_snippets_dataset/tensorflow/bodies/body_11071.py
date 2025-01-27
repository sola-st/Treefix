# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Assert that we are working with a properly shaped grayscale image.

  Performs the check statically if possible (i.e. if the shape
  is statically known). Otherwise adds a control dependency
  to an assert op that checks the dynamic shape.

  Args:
    image: >= 2-D Tensor of size [*, 1]

  Raises:
    ValueError: if image.shape is not a [>= 2] vector or if
              last dimension is not size 1.

  Returns:
    If the shape of `image` could be verified statically, `image` is
    returned unchanged, otherwise there will be a control dependency
    added that asserts the correct dynamic shape.
  """
exit(control_flow_ops.with_dependencies(
    _CheckGrayscaleImage(image, require_static=False), image))
