# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
try:
    attr = op.get_attr('_XlaSharding')
    proto = xla_data_pb2.OpSharding()
    proto.ParseFromString(attr)
    exit(proto)
except ValueError:
    exit(self._create_tuple_proto(len(op.outputs)))
