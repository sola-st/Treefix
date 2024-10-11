# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""All-reduce the `value` across all replicas so that all get the result.

    `value` can be a nested structure of tensors or `IndexedSlices`. The
    implementation should generally batch the all-reduces when possible.
    `options` can be set to hint the batching behavior.

    This API must be called in a replica context.

    Args:
      reduce_op: A `tf.distribute.ReduceOp` value specifying how values should
        be combined.
      value: Value to be reduced. A tensor or a nested structure of tensors or
        `IndexedSlices`.
      replica_id: An interger indicating the id of the replica where this
        all_reduce is called under. This is the local replica id that ranges
        from 0 to len(local_devices) - 1.
      options: A `tf.distribute.experimental.CommunicationOptions`.

    Returns:
      A tensor/IndexedSlices or a nested strucutre of tensors/IndexedSlices with
      the reduced values. The structure is the same as `value`.
    """
raise NotImplementedError("_all_reduce must be implemented in descendants.")
