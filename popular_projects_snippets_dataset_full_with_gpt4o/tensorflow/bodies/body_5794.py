# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
cluster_resolver = resolver.TPUClusterResolver(tpu='local')
self.assertIsNone(cluster_resolver._tpu_topology)

# Test set with tpu topology proto.
cluster_resolver.set_tpu_topology(
    serialized_tpu_topology=topology_pb2.TopologyProto(
        mesh_shape=[1, 1, 1, 1]).SerializeToString())
self.assertIsInstance(cluster_resolver.tpu_hardware_feature,
                      topology_pb2.TPUHardwareFeature)
