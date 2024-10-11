# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Enqueues one element to this queue.

    If the queue is full when this operation executes, it will block
    until the element has been enqueued.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed before this operation runs,
    `tf.errors.CancelledError` will be raised. If this operation is
    blocked, and either (i) the queue is closed by a close operation
    with `cancel_pending_enqueues=True`, or (ii) the session is
    `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary containing
        the values to enqueue.
      name: A name for the operation (optional).

    Returns:
      The operation that enqueues a new tuple of tensors to the queue.
    """
with ops.name_scope(name, "%s_enqueue" % self._name,
                    self._scope_vals(vals)) as scope:
    vals = self._check_enqueue_dtypes(vals)

    # NOTE(mrry): Not using a shape function because we need access to
    # the `QueueBase` object.
    for val, shape in zip(vals, self._shapes):
        val.get_shape().assert_is_compatible_with(shape)

    if self._queue_ref.dtype == _dtypes.resource:
        exit(gen_data_flow_ops.queue_enqueue_v2(
            self._queue_ref, vals, name=scope))
    else:
        exit(gen_data_flow_ops.queue_enqueue(
            self._queue_ref, vals, name=scope))
