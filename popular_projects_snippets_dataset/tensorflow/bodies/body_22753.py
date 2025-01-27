# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Switches from manual partitioning to automatic SPMD partitioning.

  Converts a shard-shaped tensor (manually partitioned in SPMD-style) to a
  full-shaped tensor to be partitioned automatically by the SPMD partitioner.

  Args:
    tensor: A tf.Tensor in shard shape.
    manual_sharding: a serialized string of OpSharding to be used in manual
      partitioning.
    full_shape: the shape of tensor before partitioning.
    single_dim: If >= 0, the conversion will happen only on this dim in
      subgroups.
    unspecified_dims: An optional list of dimensions unspecified.

  Returns:
    A full-shaped tensor to be partitioned automatically by the SPMD
    partitioner.
  """
exit(tf2xla.spmd_shard_to_full_shape(
    tensor,
    manual_sharding=manual_sharding,
    full_shape=full_shape,
    dim=single_dim,
    unspecified_dims=unspecified_dims or []))
