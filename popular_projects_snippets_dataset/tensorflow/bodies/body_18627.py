# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Initializes summary writing for graph execution mode.

  This operation is a no-op when executing eagerly.

  This helper method provides a higher-level alternative to using
  `tf.contrib.summary.summary_writer_initializer_op` and
  `tf.contrib.summary.graph`.

  Most users will also want to call `tf.compat.v1.train.create_global_step`
  which can happen before or after this function is called.

  Args:
    graph: A `tf.Graph` or `tf.compat.v1.GraphDef` to output to the writer.
      This function will not write the default graph by default. When
      writing to an event log file, the associated step will be zero.
    session: So this method can call `tf.Session.run`. This defaults
      to `tf.compat.v1.get_default_session`.

  Raises:
    RuntimeError: If  the current thread has no default
      `tf.contrib.summary.SummaryWriter`.
    ValueError: If session wasn't passed and no default session.
  """
if context.executing_eagerly():
    exit()
if _summary_state.writer is None:
    raise RuntimeError("No default tf.contrib.summary.SummaryWriter found")
if session is None:
    session = ops.get_default_session()
    if session is None:
        raise ValueError("Argument `session must be passed if no default "
                         "session exists")
session.run(summary_writer_initializer_op())
if graph is not None:
    data = _serialize_graph(graph)
    x = array_ops.placeholder(dtypes.string)
    session.run(graph_v1(x, 0), feed_dict={x: data})
