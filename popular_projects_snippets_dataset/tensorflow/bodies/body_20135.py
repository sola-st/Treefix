# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Generates the device-side Op to dequeue a tuple from the queue.

    Implicitly freezes the queue configuration if it is not already
    frozen, which will raise errors if the shapes and types have not
    been fully specified.

    Args:
      tpu_device: The TPU device ordinal where the infeed instruction should be
        placed. If None, no explicit placement will be performed, and it is up
        to the user to call this API from within a proper TPU device scope.
        The XLA code will fail if the TPU dequeue instruction is not bound to
        any device.

    Returns:
      A list of Outputs corresponding to a shard of infeed dequeued
      into XLA, suitable for use within a replicated block.

    Raises:
      ValueError: if the types or shapes of the tuple elements have not been
      set; or if a dequeue op has already been generated.
    """
self.freeze()
if self._generated_dequeue_op and not ops.inside_function():
    raise ValueError("Can't generate two dequeue Ops from the same queue")
self._generated_dequeue_op = True
full_name = "%s/dequeue" % self._name
sharded_shapes = [
    policy.get_unpartitioned_shape(policy.get_sharded_shape(shape))
    for (shape, policy) in zip(self._tuple_shapes, self._sharding_policies)
]
if tpu_device is not None:
    with ops.device(tpu_name_util.core(tpu_device)):
        dequeue_op = tpu_ops.infeed_dequeue_tuple(
            dtypes=self._tuple_types, shapes=sharded_shapes, name=full_name)
else:
    dequeue_op = tpu_ops.infeed_dequeue_tuple(
        dtypes=self._tuple_types, shapes=sharded_shapes, name=full_name)
if self._number_of_partitions <= 1:
    exit(dequeue_op)
partitions = [
    policy.get_unpartitioned_shape([1] * shape.ndims).as_list()
    for (shape, policy) in zip(self._tuple_shapes, self._sharding_policies)
]
exit(tag_sharding_attribute_for_dequeued_tensors(dequeue_op, partitions))
