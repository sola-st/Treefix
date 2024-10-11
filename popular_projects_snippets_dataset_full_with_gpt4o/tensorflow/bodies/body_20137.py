# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Generates the host-side Ops to enqueue the shards of a tuple.

    sharded_inputs is a list, one for each shard, of lists of
    Tensors. sharded_inputs[i] is the tuple of Tensors to use to feed
    shard i of the queue. Returns the host-side Ops that must be run to
    enqueue the sharded tuple. The Op for shard i is colocated with the inputs
    for shard i.

    Implicitly freezes the queue configuration if it is not already
    frozen. If the configuration has already been frozen, and is not
    compatible with the types and shapes of sharded_inputs, an error
    will be raised.

    Args:
      sharded_inputs: a list of lists of Tensors. The length of the outer list
        determines the number of shards. Each inner list indicates the types
        and shapes of the tuples in the corresponding shard.
      tpu_ordinal_function: if not None, a function that takes the
        shard index as input and returns the ordinal of the TPU device
        the shard's infeed should be placed on. tpu_ordinal_function must be
        set if the inputs are placed on CPU devices.
      placement_function: if not None, a function that takes the shard index as
        input and returns the host device where the enqueue op should be placed
        on.

    Returns:
      A list of host-side Ops, one for each shard, that when executed together
      will enqueue a full-size element of infeed.

    Raises:
      ValueError: if the queue configuration has previously been frozen and the
        shapes of the elements of sharded_inputs are not compatible with the
        frozen configuration; or if the shapes of the elements of sharded_inputs
        don't form a consistent unsharded tuple; or if the elements of a tuple
        have different device constraints.
      TypeError: if the queue configuration has previously been frozen and the
        types of the elements of sharded_inputs are not compatible with the
        frozen configuration; or if the types of the elements of sharded_inputs
        don't form a consistent unsharded tuple.
    """
self.set_configuration_from_sharded_input_tensors(sharded_inputs)
self.freeze()
if self._generated_enqueue_ops and not ops.inside_function():
    raise ValueError("Can't generate two enqueue Ops from the same queue")
self._generated_enqueue_ops = True
if tpu_ordinal_function is None:
    tpu_ordinal_function = lambda index: -1
name_prefix = "%s/enqueue" % self._name
exit([
    self._generate_enqueue_op(
        shard,
        name_prefix,
        index,
        tpu_ordinal=tpu_ordinal_function(index),
        device=placement_function(index) if placement_function else None)
    for (shard, index) in zip(sharded_inputs, range(self.number_of_shards))
])
