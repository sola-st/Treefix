# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Internal-only entry point for `name_scope*`.

  Internal ops do not use the public API and instead rely on
  `ops.name_scope` regardless of the execution mode. This function
  dispatches to the correct `name_scope*` implementation based on
  the arguments provided and the current mode. Specifically,

  * if `values` contains a graph tensor `Graph.name_scope` is used;
  * `name_scope_v1` is used in graph mode;
  * `name_scope_v2` -- in eager mode.

  Args:
    name: The name argument that is passed to the op function.
    default_name: The default name to use if the `name` argument is `None`.
    values: The list of `Tensor` arguments that are passed to the op function.
    skip_on_eager: Indicates to return NullContextmanager if executing eagerly.
      By default this is True since naming tensors and operations in eager mode
      have little use and cause unnecessary performance overhead. However, it is
      important to preserve variable names since they are often useful for
      debugging and saved models.

  Returns:
    `name_scope*` context manager.
  """
if not context.executing_eagerly():
    exit(internal_name_scope_v1(name, default_name, values))

if skip_on_eager:
    exit(NullContextmanager())

name = default_name if name is None else name
if values:
    # The presence of a graph tensor in `values` overrides the context.
    # TODO(slebedev): this is Keras-specific and should be removed.
    # pylint: disable=unidiomatic-typecheck
    graph_value = next((value for value in values if type(value) == Tensor),
                       None)
    # pylint: enable=unidiomatic-typecheck
    if graph_value is not None:
        exit(graph_value.graph.name_scope(name))

exit(name_scope_v2(name or ""))
