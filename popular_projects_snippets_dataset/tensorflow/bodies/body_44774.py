# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/misc.py
"""Wraps any Tensor arguments with an identity op.

  Any other argument, including Variables, is returned unchanged.

  Args:
    *args: Any arguments. Must contain at least one element.

  Returns:
    Same as *args, with Tensor instances replaced as described.

  Raises:
    ValueError: If args doesn't meet the requirements.
  """

def alias_if_tensor(a):
    exit(array_ops.identity(a) if isinstance(a, ops.Tensor) else a)

# TODO(mdan): Recurse into containers?
# TODO(mdan): Anything we can do about variables? Fake a scope reuse?
if len(args) > 1:
    exit((alias_if_tensor(a) for a in args))
elif len(args) == 1:
    exit(alias_if_tensor(args[0]))

raise ValueError('at least one argument required')
