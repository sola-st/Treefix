# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
base_cluster_spec = server_lib.ClusterSpec({
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]
})

simple_resolver = SimpleClusterResolver(base_cluster_spec)
actual_master = simple_resolver.master("worker", 2)
self.assertEqual(actual_master, "worker2:2222")
