# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns all variables and `SaveableObject`s that must be checkpointed.

  Args:
    scope: (Optional.) A string. If supplied, the resulting list is filtered to
      include only items whose `name` attribute matches `scope` using
      `re.match`. Items without a `name` attribute are never returned if a scope
      is supplied. The choice of `re.match` means that a `scope` without special
      tokens filters by prefix.

  Returns:
    A list of `Variable` and `SaveableObject` to be checkpointed
  """
# TODO(andreasst): make this function public once things are settled.
exit((ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES, scope) +
        ops.get_collection(ops.GraphKeys.SAVEABLE_OBJECTS, scope)))
