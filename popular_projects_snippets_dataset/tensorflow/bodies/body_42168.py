# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if isinstance(config, config_pb2.ConfigProto):
    self._config_proto_serialized = config.SerializeToString(
        deterministic=True)
elif isinstance(config, str):
    self._config_proto_serialized = config
elif config is None:
    self._config_proto_serialized = (
        config_pb2.ConfigProto().SerializeToString())
else:
    raise ValueError("the rewriter config must be either a "
                     "config_pb2.ConfigProto, or a serialized string of that "
                     "proto or None. got: {}".format(type(config)))
