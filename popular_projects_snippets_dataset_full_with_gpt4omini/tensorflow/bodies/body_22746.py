# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a tensor that has tiled sharding.

  Args:
    tensor: A tf.Tensor to shard.
    tile_assignment: An np.ndarray describing the topology of the tiling and
      which device will compute which part of the topology.
    assign_tuple_sharding: If the sharding type should be a tuple.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    unspecified_dims: An optional list of dimensions unspecified.
  """
exit(Sharding.tile(tile_assignment).apply_to_tensor(
    tensor,
    assign_tuple_sharding=assign_tuple_sharding,
    use_sharding_op=use_sharding_op,
    unspecified_dims=unspecified_dims or []))
