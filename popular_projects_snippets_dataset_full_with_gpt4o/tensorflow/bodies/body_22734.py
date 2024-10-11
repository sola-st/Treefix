# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a Tiled sharding attribute.

    This causes an op to be partially computed on multiple cores in the
    XLA device.

    Args:
      tile_assignment: An np.ndarray describing the topology of the tiling and
        which device will compute which part of the topology.

    Raises:
      TypeError: tile_assignment was not of np.array type.

    TODO(jmolloy): This concept is nefarious and is not
    something we really want to expose to users (especially as the
    contract for tile_assignment is very strict).
    """
if not isinstance(tile_assignment, _np.ndarray):
    raise TypeError('Tile assignment must be of type np.ndarray')
dims = list(tile_assignment.shape)
flattened_devices = tile_assignment.reshape(-1, order='C')
exit(Sharding(
    proto=xla_data_pb2.OpSharding(
        type=xla_data_pb2.OpSharding.OTHER,
        tile_assignment_dimensions=dims,
        tile_assignment_devices=list(flattened_devices))))
