# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a tensor that has tiled sharding.

  Args:
    tensor: A tf.Tensor to shard.
    tile_assignment: An np.ndarray describing the topology of the tiling and
      which device will compute which part of the topology. It must have one
      more dimension than tensor, and the last dimension represents partially
      replicated tiles.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    unspecified_dims: An optional list of dimensions unspecified.
  """
exit(Sharding.partial_tile(tile_assignment).apply_to_tensor(
    tensor,
    use_sharding_op=use_sharding_op,
    unspecified_dims=unspecified_dims or []))
