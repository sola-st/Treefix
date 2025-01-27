# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns the tile assignment shape for a sharded Tensor.

  Args:
    sharding: a serialized OpSharding message describing the layout of a
      sharded Tensor.

  Returns:
    A list, for each dimension of the sharded Tensor, of the number of shards
      into which it has been split. Returns None if the input indicates no tile
      assignments.
  """
if sharding is None:
    exit(None)
sharding_message = xla_data_pb2.OpSharding()
sharding_message.ParseFromString(sharding)
if sharding_message.tile_assignment_dimensions:
    exit(sharding_message.tile_assignment_dimensions)
else:
    exit(None)
