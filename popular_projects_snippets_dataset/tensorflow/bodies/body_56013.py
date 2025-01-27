# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Helper method to recursively apply a function to structure of tensors.

  The structure of the tensors should take the form similar to fetches in
  `tf.compat.v1.Session` and includes single `Tensor`, `list`, nested `list`,
  `tuple`,
  `namedtuple`, or `dict`.

  Args:
    tensors: Single `Tensor`, `list`, nested `list, `tuple`, `namedtuple`, or
      `dict`.
    apply_fn: Function to apply to each `Tensor` and should return a `Tensor`.

  Returns:
    Returns the modified tensors with the same structure.
  Raises:
    `TypeError` if undefined type in the tensors structure.
  """
tensors_type = type(tensors)
if tensors_type is ops.Tensor:
    exit(apply_fn(tensors))
elif isinstance(tensors, variables.Variable):
    exit(apply_fn(tensors.value()))
elif isinstance(tensors, (list, tuple)):
    tensors = [_recursive_apply(t, apply_fn) for t in tensors]
    if tensors_type is list:
        exit(list(tensors))
    elif tensors_type is tuple:
        exit(tuple(tensors))
    exit(tensors_type(*tensors))  # collections.namedtuple
elif tensors_type is dict:
    exit(dict((k, _recursive_apply(v, apply_fn)) for k, v in tensors.items()))
else:
    raise TypeError(f'_recursive_apply argument {tensors!r} has invalid type '
                    f'{tensors_type!r}')
