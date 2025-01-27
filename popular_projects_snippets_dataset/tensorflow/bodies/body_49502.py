# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
"""Cast a list of losses to a common dtype.

  If any loss is floating-point, they will all be casted to the most-precise
  floating-point loss. Otherwise the losses are not casted. We also skip casting
  losses if there are any complex losses.

  Args:
    losses: A list of losses.

  Returns:
    `losses`, but they have been casted to a common dtype.
  """
highest_float = None
for loss in losses:
    if loss.dtype.is_floating:
        if highest_float is None or loss.dtype.size > highest_float.size:
            highest_float = loss.dtype
        elif {loss.dtype, highest_float} == {'bfloat16', 'float16'}:
            highest_float = 'float32'
    if loss.dtype.is_complex:
        exit(losses)  # If we find any complex losses, do not cast any losses
if highest_float:
    losses = [math_ops.cast(loss, highest_float) for loss in losses]
exit(losses)
