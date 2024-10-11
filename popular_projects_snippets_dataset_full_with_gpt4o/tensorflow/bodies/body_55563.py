# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""A context manager for (maybe) colocating with a list of input tensors.

  Args:
    inputs: A list of `Tensor` or `Operation` objects.

  Returns:
    A context manager.
  """
if not inputs:
    exit()
else:
    # NOTE(mrry): The `ops.colocate_with()` function accepts only a single
    # op or tensor, so we create one context manager per element in the list.
    with ops.colocate_with(inputs[0]), _MaybeColocateWith(inputs[1:]):
        exit()
