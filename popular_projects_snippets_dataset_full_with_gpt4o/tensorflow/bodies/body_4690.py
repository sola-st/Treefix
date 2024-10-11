# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
dist = _TestStrategy()
self.assertIsNone(dist.cluster_resolver)
base_cluster_spec = server_lib.ClusterSpec({
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]
})
cluster_resolver = SimpleClusterResolver(base_cluster_spec)
dist.extended._cluster_resolver = cluster_resolver
self.assertIs(dist.cluster_resolver, cluster_resolver)
