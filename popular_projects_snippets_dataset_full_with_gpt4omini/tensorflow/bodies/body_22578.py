# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Create a QueueRunner from arguments.

    Args:
      queue: A `Queue`.
      enqueue_ops: List of enqueue ops to run in threads later.
      close_op: Op to close the queue. Pending enqueue ops are preserved.
      cancel_op: Op to close the queue and cancel pending enqueue ops.
      queue_closed_exception_types: Tuple of exception types, which indicate
        the queue has been safely closed.

    Raises:
      ValueError: If `queue` or `enqueue_ops` are not provided when not
        restoring from `queue_runner_def`.
      TypeError: If `queue_closed_exception_types` is provided, but is not
        a non-empty tuple of error types (subclasses of `tf.errors.OpError`).
    """
if not queue or not enqueue_ops:
    raise ValueError("Must provide queue and enqueue_ops.")
self._queue = queue
self._enqueue_ops = enqueue_ops
self._close_op = close_op
self._cancel_op = cancel_op
if queue_closed_exception_types is not None:
    if (not isinstance(queue_closed_exception_types, tuple)
        or not queue_closed_exception_types
        or not all(issubclass(t, errors.OpError)
                   for t in queue_closed_exception_types)):
        raise TypeError(
            "queue_closed_exception_types, when provided, "
            "must be a tuple of tf.error types, but saw: %s"
            % queue_closed_exception_types)
self._queue_closed_exception_types = queue_closed_exception_types
# Close when no more will be produced, but pending enqueues should be
# preserved.
if self._close_op is None:
    self._close_op = self._queue.close()
# Close and cancel pending enqueues since there was an error and we want
# to unblock everything so we can cleanly exit.
if self._cancel_op is None:
    self._cancel_op = self._queue.close(cancel_pending_enqueues=True)
if not self._queue_closed_exception_types:
    self._queue_closed_exception_types = (errors.OutOfRangeError,)
else:
    self._queue_closed_exception_types = tuple(
        self._queue_closed_exception_types)
