# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Converts this `QueueRunner` to a `QueueRunnerDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `QueueRunnerDef` protocol buffer, or `None` if the `Variable` is not in
      the specified name scope.
    """
if (export_scope is None or
    self.queue.name.startswith(export_scope)):
    queue_runner_def = queue_runner_pb2.QueueRunnerDef()
    queue_runner_def.queue_name = ops.strip_name_scope(
        self.queue.name, export_scope)
    for enqueue_op in self.enqueue_ops:
        queue_runner_def.enqueue_op_name.append(
            ops.strip_name_scope(enqueue_op.name, export_scope))
    queue_runner_def.close_op_name = ops.strip_name_scope(
        self.close_op.name, export_scope)
    queue_runner_def.cancel_op_name = ops.strip_name_scope(
        self.cancel_op.name, export_scope)
    queue_runner_def.queue_closed_exception_types.extend([
        errors.error_code_from_exception_type(cls)
        for cls in self._queue_closed_exception_types])
    exit(queue_runner_def)
else:
    exit(None)
