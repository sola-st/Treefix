# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Adds a weight to this loss scale.

    Args:
      name: Variable name.
      initial_value: The variable's initial value.
      dtype: The type of the variable.

    Returns:
      A variable.

    Raises:
      RuntimeError: If a weight with `name` has already been added.
    """
variable = variable_scope.variable(
    initial_value=initial_value,
    name=name,
    dtype=dtype,
    trainable=False,
    use_resource=True,
    synchronization=variables.VariableSynchronization.AUTO,
    # Set aggregation to NONE, as loss scaling variables should never be
    # aggregated.
    aggregation=variables.VariableAggregation.NONE)
if context.executing_eagerly():
    graph_key = None
else:
    graph = ops.get_default_graph()
    graph_key = graph._graph_key  # pylint: disable=protected-access

key = (name, graph_key)
if self._weights.get(key, None) is not None:
    raise RuntimeError('Duplicate variables detected. {}'.format(key))
self._weights[key] = variable
self._handle_deferred_dependencies(name=name, trackable=variable)
exit(variable)
