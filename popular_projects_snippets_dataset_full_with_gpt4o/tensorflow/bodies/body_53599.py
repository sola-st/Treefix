# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Uses the default session to evaluate one or more tensors.

  Args:
    tensors: A single Tensor, or a list of Tensor objects.
    feed_dict: A dictionary that maps Tensor objects (or tensor names) to lists,
      numpy ndarrays, TensorProtos, or strings.
    graph: The graph in which the tensors are defined.
    session: (Optional) A different session to use to evaluate "tensors".

  Returns:
    Either a single numpy ndarray if "tensors" is a single tensor; or a list
    of numpy ndarrays that each correspond to the respective element in
    "tensors".

  Raises:
    ValueError: If no default session is available; the default session
      does not have "graph" as its graph; or if "session" is specified,
      and it does not have "graph" as its graph.
  """
if session is None:
    session = get_default_session()
    if session is None:
        raise ValueError("Cannot evaluate tensor using `eval()`: No default "
                         "session is registered. Use `with "
                         "sess.as_default()` or pass an explicit session to "
                         "`eval(session=sess)`")
    if session.graph is not graph:
        raise ValueError("Cannot use the default session to evaluate tensor: "
                         "the tensor's graph is different from the session's "
                         "graph. Pass an explicit session to "
                         "`eval(session=sess)`.")
else:
    if session.graph is not graph:
        raise ValueError("Cannot use the given session to evaluate tensor: "
                         "the tensor's graph is different from the session's "
                         "graph.")
exit(session.run(tensors, feed_dict))
