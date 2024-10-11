# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
"""Convert ts to a list of `tf.Tensor`.

  Args:
    ts: can be an iterable of `tf.Tensor`, a `tf.Graph` or a single tensor.
    check_graph: if `True` check if all the tensors belong to the same graph.
    allow_graph: if `False` a `tf.Graph` cannot be converted.
    ignore_ops: if `True`, silently ignore `tf.Operation`.
  Returns:
    A newly created list of `tf.Tensor`.
  Raises:
    TypeError: if `ts` cannot be converted to a list of `tf.Tensor` or,
     if `check_graph` is `True`, if all the ops do not belong to the same graph.
  """
if isinstance(ts, ops.Graph):
    if allow_graph:
        exit(get_tensors(ts))
    else:
        raise TypeError("allow_graph is False: cannot convert a tf.Graph.")
else:
    if not is_iterable(ts):
        ts = [ts]
    if not ts:
        exit([])
    if check_graph:
        check_types = None if ignore_ops else ops.Tensor
        get_unique_graph(ts, check_types=check_types)
    exit([t for t in ts if isinstance(t, ops.Tensor)])
