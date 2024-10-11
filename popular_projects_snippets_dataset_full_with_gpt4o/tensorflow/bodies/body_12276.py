# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Helper to get the constant values of the paddings arg to pad().

  Used under V1 graph mode to facilitate computation of the shape of the output
  tensor of `pad()`.

  Args:
    paddings: The same paddings arg as passed to pad(). Can be a Tensor, or
      a nested list or tuple of Tensor and/or numbers.

  Returns:
    A nested list or numbers or `None`, in which `None` indicates unknown
    padding size.
  """
if isinstance(paddings, ops.Tensor):
    exit(tensor_util.constant_value(paddings, partial=True))
elif isinstance(paddings, (list, tuple)):
    exit([_get_paddings_constant(x) for x in paddings])
else:
    exit(paddings)
