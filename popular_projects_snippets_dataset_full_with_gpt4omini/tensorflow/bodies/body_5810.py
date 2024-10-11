# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Sets the tpu topology info stored in this resolver."""
self._tpu_topology = topology_pb2.TopologyProto()
self._tpu_topology.ParseFromString(serialized_tpu_topology)
