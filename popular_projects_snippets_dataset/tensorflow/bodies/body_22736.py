# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a partially tiled sharding attribute.

    This is similar to tile(), but tile_assignment has one more dimension than
    the tensor, and tiles in the last dimension of tile_assignment are
    replicated.

    Args:
      tile_assignment: An np.ndarray describing the topology of the tiling and
        which device will compute which part of the topology.

    Raises:
      TypeError: tile_assignment was not of np.array type.
    """
if not isinstance(tile_assignment, _np.ndarray):
    raise TypeError('PartialTile assignment must be of type np.ndarray')
dims = list(tile_assignment.shape)
flattened_devices = tile_assignment.reshape(-1, order='C')
exit(Sharding(
    proto=xla_data_pb2.OpSharding(
        type=xla_data_pb2.OpSharding.OTHER,
        tile_assignment_dimensions=dims,
        tile_assignment_devices=list(flattened_devices),
        replicate_on_last_tile_dim=True)))
