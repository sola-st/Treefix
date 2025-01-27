# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a manuall sharding attribute.

    This means the op is manually partitioned by the user and XLA will not
    change the shapes.
    """
exit(Sharding(
    proto=xla_data_pb2.OpSharding(type=xla_data_pb2.OpSharding.MANUAL)))
