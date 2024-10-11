# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a subgroup manual sharding attribute.

    This is similar to tile(), but tile_assignment has one or more dimension
    than the tensor, and subgroup_modes define the sharding types in the last
    dimensions of tile_assignment.

    Args:
      tile_assignment: An np.ndarray describing the topology of the tiling and
        which device will compute which part of the topology.
      subgroup_modes: sharding types for the dimension more than the tensor
        shape rank.

    Raises:
      TypeError: tile_assignment was not of np.array type or subgroup_modes
        has unsupported sharding type.
    """
if not isinstance(tile_assignment, _np.ndarray):
    raise TypeError('SubgroupTile assignment must be of type np.ndarray')

if not isinstance(subgroup_modes, list):
    raise TypeError('subgroup_modes in subgroup manual must be of type list')

if len(tile_assignment.shape) < len(subgroup_modes):
    raise TypeError('SubgroupTile assignment must have rank larger than'
                    ' length of subgroup_modes')

for sharding_type in subgroup_modes:
    if sharding_type not in [
        xla_data_pb2.OpSharding.REPLICATED, xla_data_pb2.OpSharding.MANUAL
    ]:
        raise TypeError(
            'Each sharding_type in subgroup_modes in subgroup manual must '
            'be of type xla_data_pb2.OpSharding.REPLICATED'
            ' or xla_data_pb2.OpSharding.MANUAL')
dims = list(tile_assignment.shape)
flattened_devices = tile_assignment.reshape(-1, order='C')
exit(Sharding(
    proto=xla_data_pb2.OpSharding(
        type=xla_data_pb2.OpSharding.OTHER,
        tile_assignment_dimensions=dims,
        tile_assignment_devices=list(flattened_devices),
        last_tile_dims=list(subgroup_modes))))
