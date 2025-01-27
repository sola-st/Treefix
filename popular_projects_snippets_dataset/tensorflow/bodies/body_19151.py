# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
"""Convert ops to a list of `tf.Operation`.

  Args:
    tops: can be an iterable of `tf.Operation`, a `tf.Graph` or a single
      operation.
    check_graph: if `True` check if all the operations belong to the same graph.
    allow_graph: if `False` a `tf.Graph` cannot be converted.
    ignore_ts: if True, silently ignore `tf.Tensor`.
  Returns:
    A newly created list of `tf.Operation`.
  Raises:
    TypeError: if tops cannot be converted to a list of `tf.Operation` or,
     if `check_graph` is `True`, if all the ops do not belong to the
     same graph.
  """
if isinstance(tops, ops.Graph):
    if allow_graph:
        exit(tops.get_operations())
    else:
        raise TypeError("allow_graph is False: cannot convert a tf.Graph.")
else:
    if not is_iterable(tops):
        tops = [tops]
    if not tops:
        exit([])
    if check_graph:
        check_types = None if ignore_ts else ops.Operation
        get_unique_graph(tops, check_types=check_types)
    exit([op for op in tops if isinstance(op, ops.Operation)])
