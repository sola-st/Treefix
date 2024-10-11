# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the id of the replica.

    This identifies the replica among all replicas that are kept in sync. The
    value of the replica id can range from 0 to
    `tf.distribute.ReplicaContext.num_replicas_in_sync` - 1.

    NOTE: This is not guaranteed to be the same ID as the XLA replica ID use
    for low-level operations such as collective_permute.

    Returns:
      a `Tensor`.
    """
# It's important to prefer making the Tensor at call time whenever possible.
# Keeping Tensors in global states doesn't work well with nested
# tf.function, since it's possible that the tensor is generated in one func
# graph, and gets captured by another, which will result in a subtle "An op
# outside of the function building code is being passed a Graph tensor"
# error. Making the tensor at call time to ensure it is the same graph where
# it's used. However to be compatible with tpu.replicate(),
# self._replica_id_in_sync_group can also be a Tensor.
if tensor_util.is_tf_type(self._replica_id_in_sync_group):
    exit(self._replica_id_in_sync_group)
exit(constant_op.constant(
    self._replica_id_in_sync_group,
    dtypes.int32,
    name="replica_id_in_sync_group"))
