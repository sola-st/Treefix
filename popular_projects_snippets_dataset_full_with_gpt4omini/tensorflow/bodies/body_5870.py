# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
cluster_spec_1 = server_lib.ClusterSpec({
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]
})
resolver1 = SimpleClusterResolver(cluster_spec_1, task_type="ps",
                                  task_id=1, environment="cloud",
                                  num_accelerators={"GPU": 8},
                                  rpc_layer="grpc")

cluster_spec_2 = server_lib.ClusterSpec({
    "ps": ["ps2:2222", "ps3:2222"],
    "worker": ["worker3:2222", "worker4:2222", "worker5:2222"]
})
resolver2 = SimpleClusterResolver(cluster_spec_2, task_type="worker",
                                  task_id=2, environment="local",
                                  num_accelerators={"GPU": 16},
                                  rpc_layer="http")

union_resolver = UnionClusterResolver(resolver1, resolver2)

self.assertEqual(union_resolver.task_type, "ps")
self.assertEqual(union_resolver.task_id, 1)
self.assertEqual(union_resolver.environment, "cloud")
self.assertEqual(union_resolver.num_accelerators(), {"GPU": 8})
self.assertEqual(union_resolver.rpc_layer, "grpc")

union_resolver.task_type = "worker"
union_resolver.task_id = 2
union_resolver.rpc_layer = "http"

self.assertEqual(union_resolver.task_type, "worker")
self.assertEqual(union_resolver.task_id, 2)
self.assertEqual(union_resolver.rpc_layer, "http")
