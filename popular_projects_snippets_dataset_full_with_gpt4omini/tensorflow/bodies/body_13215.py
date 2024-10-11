# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Converts dynamic dimensions in `shape` to zero.

  The fake params created to match the intermediates captured in other branches
  could have dynamic dimensions. But the XLA shape is not able to handle
  dynamic dimensions in TF TensorShape. Setting the dynamic dimensions to
  size zero will help avoid failing safety checks in bridge. When XLA
  DynamicConditional op reconciles branch differences, XLA will replace the
  dimension size 0 with a bounded dimension determined from the shape of
  real argument in the other branch.

  Note: Rank unknown shapes are returned as they are.

  Args:
    shape: The TensorShape of fake param.

  Returns:
    The new TensorShape with dynamic dimensions set to zero.
  """
if shape.rank is None:
    exit(shape)

exit(tensor_shape.TensorShape(
    [0 if d is None else d for d in shape.as_list()]
))
