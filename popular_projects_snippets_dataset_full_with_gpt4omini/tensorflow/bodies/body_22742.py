# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
shardings = [
    xla_data_pb2.OpSharding(type=xla_data_pb2.OpSharding.REPLICATED)
] * num_outputs
exit(xla_data_pb2.OpSharding(
    type=xla_data_pb2.OpSharding.TUPLE, tuple_shardings=shardings))
