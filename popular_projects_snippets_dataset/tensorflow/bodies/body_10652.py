# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Takes the given number of completed elements from this barrier.

    This operation concatenates completed-element component tensors along
    the 0th dimension to make a single component tensor.

    If barrier has no completed elements, this operation will block
    until there are 'num_elements' elements to take.

    TODO(b/25743580): the semantics of `allow_small_batch` are experimental
    and may be extended to other cases in the future.

    TODO(ebrevdo): If a take_many(allow_small_batch=True) is blocking
    already when the barrier is closed, it will block for ever. Fix this
    by using asynchronous operations.

    Args:
      num_elements: The number of elements to take.
      allow_small_batch: If the barrier is closed, don't block if there are less
        completed elements than requested, but instead return all available
        completed elements.
      timeout: This specifies the number of milliseconds to block
        before returning with DEADLINE_EXCEEDED. (This option is not
        supported yet.)
      name: A name for the operation (optional).

    Returns:
      A tuple of (index, key, value_list).
      "index" is a int64 tensor of length num_elements containing the
        index of the insert_many call for which the very first component of
        the given element was inserted into the Barrier, starting with
        the value -2**63.  Note, this value is different from the
        index of the insert_many call for which the element was completed.
      "key" is a string tensor of length num_elements containing the keys.
      "value_list" is a tuple of tensors, each one with size num_elements
        in the 0th dimension for each component in the barrier's values.

    """
if name is None:
    name = "%s_BarrierTakeMany" % self._name
ret = gen_data_flow_ops.barrier_take_many(
    self._barrier_ref,
    num_elements,
    self._types,
    allow_small_batch,
    timeout,
    name=name)

# NOTE(mrry): Not using a shape function because we need access to
# the Barrier object.
if not context.executing_eagerly():
    op = ret[0].op
    if allow_small_batch:
        batch_dim = None
    else:
        batch_dim = tensor_shape.Dimension(
            tensor_util.constant_value(op.inputs[1]))
    op.outputs[0].set_shape(tensor_shape.TensorShape([batch_dim]))  # indices
    op.outputs[1].set_shape(tensor_shape.TensorShape([batch_dim]))  # keys
    for output, shape in zip(op.outputs[2:], self._shapes):  # value_list
        output.set_shape(
            tensor_shape.TensorShape([batch_dim]).concatenate(shape))

exit(ret)
