# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Closes this queue.

    This operation signals that no more elements will be enqueued in
    the given queue. Subsequent `enqueue` and `enqueue_many`
    operations will fail. Subsequent `dequeue` and `dequeue_many`
    operations will continue to succeed if sufficient elements remain
    in the queue. Subsequently dequeue and dequeue_many operations
    that would otherwise block waiting for more elements (if close
    hadn't been called) will now fail immediately.

    If `cancel_pending_enqueues` is `True`, all pending requests will also
    be canceled.

    Args:
      cancel_pending_enqueues: (Optional.) A boolean, defaulting to
        `False` (described above).
      name: A name for the operation (optional).

    Returns:
      The operation that closes the queue.
    """
if name is None:
    name = "%s_Close" % self._name
if self._queue_ref.dtype == _dtypes.resource:
    exit(gen_data_flow_ops.queue_close_v2(
        self._queue_ref,
        cancel_pending_enqueues=cancel_pending_enqueues,
        name=name))
else:
    exit(gen_data_flow_ops.queue_close(
        self._queue_ref,
        cancel_pending_enqueues=cancel_pending_enqueues,
        name=name))
