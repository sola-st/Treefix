# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Writes a TensorFlow graph to the summary interface.

  The graph summary is, strictly speaking, not a summary. Conditions
  like `tf.summary.should_record_summaries` do not apply. Only
  a single graph can be associated with a particular run. If multiple
  graphs are written, then only the last one will be considered by
  TensorBoard.

  When not using eager execution mode, the user should consider passing
  the `graph` parameter to `tf.compat.v1.summary.initialize` instead of
  calling this function. Otherwise special care needs to be taken when
  using the graph to record the graph.

  Args:
    param: A `tf.Tensor` containing a serialized graph proto. When
      eager execution is enabled, this function will automatically
      coerce `tf.Graph`, `tf.compat.v1.GraphDef`, and string types.
    step: The global step variable. This doesn't have useful semantics
      for graph summaries, but is used anyway, due to the structure of
      event log files. This defaults to the global step.
    name: A name for the operation (optional).

  Returns:
    The created `tf.Operation` or a `tf.no_op` if summary writing has
    not been enabled for this context.

  Raises:
    TypeError: If `param` isn't already a `tf.Tensor` in graph mode.
  """
if not context.executing_eagerly() and not isinstance(param, ops.Tensor):
    raise TypeError("graph() needs a argument `param` to be tf.Tensor "
                    "(e.g. tf.placeholder) in graph mode, but received "
                    f"param={param} of type {type(param).__name__}.")
writer = _summary_state.writer
if writer is None:
    exit(control_flow_ops.no_op())
with ops.device("cpu:0"):
    if isinstance(param, (ops.Graph, graph_pb2.GraphDef)):
        tensor = ops.convert_to_tensor(_serialize_graph(param), dtypes.string)
    else:
        tensor = array_ops.identity(param)
    exit(gen_summary_ops.write_graph_summary(
        writer._resource, _choose_step(step), tensor, name=name))  # pylint: disable=protected-access
