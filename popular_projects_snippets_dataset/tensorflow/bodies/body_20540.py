# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
"""Returns a session given a timeout and a cluster configuration."""
config_proto = config_pb2.ConfigProto(
    operation_timeout_in_ms=timeout_in_secs, cluster_def=cluster_def)
exit(config_proto)
