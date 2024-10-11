# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Enqueues zero or more elements to this queue.

    This operation slices each component tensor along the 0th dimension to
    make multiple queue elements. All of the tensors in `vals` must have the
    same size in the 0th dimension.

    If the queue is full when this operation executes, it will block
    until all of the elements have been enqueued.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed before this operation runs,
    `tf.errors.CancelledError` will be raised. If this operation is
    blocked, and either (i) the queue is closed by a close operation
    with `cancel_pending_enqueues=True`, or (ii) the session is
    `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary
        from which the queue elements are taken.
      name: A name for the operation (optional).

    Returns:
      The operation that enqueues a batch of tuples of tensors to the queue.
    """
with ops.name_scope(name, "%s_EnqueueMany" % self._name,
                    self._scope_vals(vals)) as scope:
    vals = self._check_enqueue_dtypes(vals)

    # NOTE(mrry): Not using a shape function because we need access to
    # the `QueueBase` object.
    # NOTE(fchollet): the code that follow is verbose because it needs to be
    # compatible with both TF v1 TensorShape behavior and TF v2 behavior.
    batch_dim = tensor_shape.dimension_value(
        vals[0].get_shape().with_rank_at_least(1)[0])
    batch_dim = tensor_shape.Dimension(batch_dim)
    for val, shape in zip(vals, self._shapes):
        val_batch_dim = tensor_shape.dimension_value(
            val.get_shape().with_rank_at_least(1)[0])
        val_batch_dim = tensor_shape.Dimension(val_batch_dim)
        batch_dim = batch_dim.merge_with(val_batch_dim)
        val.get_shape()[1:].assert_is_compatible_with(shape)

    exit(gen_data_flow_ops.queue_enqueue_many_v2(
        self._queue_ref, vals, name=scope))
