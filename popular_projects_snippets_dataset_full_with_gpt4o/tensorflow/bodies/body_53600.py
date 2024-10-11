# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Uses the default session to run "operation".

  Args:
    operation: The Operation to be run.
    feed_dict: A dictionary that maps Tensor objects (or tensor names) to lists,
      numpy ndarrays, TensorProtos, or strings.
    graph: The graph in which "operation" is defined.
    session: (Optional) A different session to use to run "operation".

  Raises:
    ValueError: If no default session is available; the default session
      does not have "graph" as its graph; or if "session" is specified,
      and it does not have "graph" as its graph.
  """
if session is None:
    session = get_default_session()
    if session is None:
        raise ValueError("Cannot execute operation using `run()`: No default "
                         "session is registered. Use `with "
                         "sess.as_default():` or pass an explicit session to "
                         "`run(session=sess)`")
    if session.graph is not graph:
        raise ValueError("Cannot use the default session to execute operation: "
                         "the operation's graph is different from the "
                         "session's graph. Pass an explicit session to "
                         "run(session=sess).")
else:
    if session.graph is not graph:
        raise ValueError("Cannot use the given session to execute operation: "
                         "the operation's graph is different from the session's "
                         "graph.")
session.run(operation, feed_dict)
