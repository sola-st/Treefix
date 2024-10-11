# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns an AssignDevice sharding attribute.

    This causes an op to be computed in its entirety only on one core in
    the XLA device.
    Args:
      core: The core to assign this Op to.
    """
exit(Sharding(
    proto=xla_data_pb2.OpSharding(
        type=xla_data_pb2.OpSharding.MAXIMAL,
        tile_assignment_dimensions=[1],
        tile_assignment_devices=[core])))
