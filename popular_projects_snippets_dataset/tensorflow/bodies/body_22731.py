# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a replicated sharding attribute.

    This causes an op to be computed in its entirety independently on all
    cores in the XLA device.
    """
exit(Sharding(
    proto=xla_data_pb2.OpSharding(type=xla_data_pb2.OpSharding.REPLICATED)))
