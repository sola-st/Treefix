# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns all variables created with `trainable=True`.

  When passed `trainable=True`, the `Variable()` constructor automatically
  adds new variables to the graph collection
  `GraphKeys.TRAINABLE_VARIABLES`. This convenience function returns the
  contents of that collection.

  @compatibility(TF2)
  Not compatible with eager execution and `tf.function`. In particular, Graph
  collections are deprecated in TF2. Instead please create a `tf.Module`
  container for all your model state, including variables.
  You can then list all the trainable variables in your `tf.Module` through the
  `trainable_variables` attribute.
  @end_compatibility

  Args:
    scope: (Optional.) A string. If supplied, the resulting list is filtered to
      include only items whose `name` attribute matches `scope` using
      `re.match`. Items without a `name` attribute are never returned if a scope
      is supplied. The choice of `re.match` means that a `scope` without special
      tokens filters by prefix.

  Returns:
    A list of Variable objects.
  """
exit(ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES, scope))
