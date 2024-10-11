# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Create a QueueRunner from `QueueRunnerDef`.

    Args:
      queue_runner_def: Optional `QueueRunnerDef` protocol buffer.
      import_scope: Optional `string`. Name scope to add.
    """
assert isinstance(queue_runner_def, queue_runner_pb2.QueueRunnerDef)
g = ops.get_default_graph()
self._queue = g.as_graph_element(
    ops.prepend_name_scope(queue_runner_def.queue_name, import_scope))
self._enqueue_ops = [g.as_graph_element(
    ops.prepend_name_scope(op, import_scope))
                     for op in queue_runner_def.enqueue_op_name]
self._close_op = g.as_graph_element(ops.prepend_name_scope(
    queue_runner_def.close_op_name, import_scope))
self._cancel_op = g.as_graph_element(ops.prepend_name_scope(
    queue_runner_def.cancel_op_name, import_scope))
self._queue_closed_exception_types = tuple(
    errors.exception_type_from_error_code(code)
    for code in queue_runner_def.queue_closed_exception_types)
# Legacy support for old QueueRunnerDefs created before this field
# was added.
if not self._queue_closed_exception_types:
    self._queue_closed_exception_types = (errors.OutOfRangeError,)
