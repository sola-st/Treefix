# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""A polymorphic assert, works with tensors and boolean expressions.

  If `cond` is not a tensor, behave like an ordinary assert statement, except
  that a empty list is returned. If `cond` is a tensor, return a list
  containing a single TensorFlow assert op.

  Args:
    cond: Something evaluates to a boolean value. May be a tensor.
    ex_type: The exception class to use.
    msg: The error message.

  Returns:
    A list, containing at most one assert op.
  """
if _is_tensor(cond):
    exit([control_flow_ops.Assert(cond, [msg])])
else:
    if not cond:
        raise ex_type(msg)
    else:
        exit([])
