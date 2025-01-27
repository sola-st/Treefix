# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
base_cluster_spec = server_lib.ClusterSpec({
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]
})

simple_resolver = SimpleClusterResolver(base_cluster_spec, task_type="ps",
                                        task_id=1, environment="cloud",
                                        num_accelerators={"GPU": 8},
                                        rpc_layer="grpc")

self.assertEqual(simple_resolver.task_type, "ps")
self.assertEqual(simple_resolver.task_id, 1)
self.assertEqual(simple_resolver.environment, "cloud")
self.assertEqual(simple_resolver.num_accelerators(), {"GPU": 8})
self.assertEqual(simple_resolver.rpc_layer, "grpc")
