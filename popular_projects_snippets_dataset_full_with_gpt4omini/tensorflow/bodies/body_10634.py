# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Dequeues one element from this queue.

    If the queue is empty when this operation executes, it will block
    until there is an element to dequeue.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed, the queue is empty, and there are no pending
    enqueue operations that can fulfill this request,
    `tf.errors.OutOfRangeError` will be raised. If the session is
    `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      name: A name for the operation (optional).

    Returns:
      The tuple of tensors that was dequeued.
    """
if name is None:
    name = "%s_Dequeue" % self._name
if self._queue_ref.dtype == _dtypes.resource:
    ret = gen_data_flow_ops.queue_dequeue_v2(
        self._queue_ref, self._dtypes, name=name)
else:
    ret = gen_data_flow_ops.queue_dequeue(
        self._queue_ref, self._dtypes, name=name)

# NOTE(mrry): Not using a shape function because we need access to
# the `QueueBase` object.
if not context.executing_eagerly():
    op = ret[0].op
    for output, shape in zip(op.values(), self._shapes):
        output.set_shape(shape)

exit(self._dequeue_return_value(ret))
