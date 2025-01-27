# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns the set of tensors/ops reachable from `inputs`.

  Stops if all targets have been found (target is optional).

  Only valid in Symbolic mode, not Eager mode.

  Args:
    inputs: List of tensors.
    targets: List of tensors.

  Returns:
    A set of tensors reachable from the inputs (includes the inputs themselves).
  """
inputs = nest.flatten(inputs, expand_composites=True)
reachable = object_identity.ObjectIdentitySet(inputs)
if targets:
    remaining_targets = object_identity.ObjectIdentitySet(nest.flatten(targets))
queue = collections.deque(inputs)

while queue:
    x = queue.pop()
    if isinstance(x, tuple(_user_convertible_tensor_types)):
        # Can't find consumers of user-specific types.
        continue

    if isinstance(x, ops.Operation):
        outputs = x.outputs[:] or []
        outputs += x._control_outputs  # pylint: disable=protected-access
    elif isinstance(x, variables.Variable):
        try:
            outputs = [x.op]
        except AttributeError:
            # Variables can be created in an Eager context.
            outputs = []
    elif tensor_util.is_tf_type(x):
        outputs = x.consumers()
    else:
        raise TypeError('Expected Operation, Variable, or Tensor, got ' + str(x))

    for y in outputs:
        if y not in reachable:
            reachable.add(y)
            if targets:
                remaining_targets.discard(y)
            queue.appendleft(y)

    if targets and not remaining_targets:
        exit(reachable)

exit(reachable)
