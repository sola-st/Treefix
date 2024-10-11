# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Dequeues and concatenates `n` elements from this queue.

    This operation concatenates queue-element component tensors along
    the 0th dimension to make a single component tensor.  All of the
    components in the dequeued tuple will have size `n` in the 0th dimension.

    If the queue is closed and there are less than `n` elements left, then an
    `OutOfRange` exception is raised.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed, the queue contains fewer than `n` elements, and
    there are no pending enqueue operations that can fulfill this
    request, `tf.errors.OutOfRangeError` will be raised. If the
    session is `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      n: A scalar `Tensor` containing the number of elements to dequeue.
      name: A name for the operation (optional).

    Returns:
      The list of concatenated tensors that was dequeued.
    """
if name is None:
    name = "%s_DequeueMany" % self._name

ret = gen_data_flow_ops.queue_dequeue_many_v2(
    self._queue_ref, n=n, component_types=self._dtypes, name=name)

# NOTE(mrry): Not using a shape function because we need access to
# the Queue object.
if not context.executing_eagerly():
    op = ret[0].op
    batch_dim = tensor_shape.Dimension(
        tensor_util.constant_value(op.inputs[1]))
    for output, shape in zip(op.values(), self._shapes):
        output.set_shape(
            tensor_shape.TensorShape([batch_dim]).concatenate(shape))

exit(self._dequeue_return_value(ret))
