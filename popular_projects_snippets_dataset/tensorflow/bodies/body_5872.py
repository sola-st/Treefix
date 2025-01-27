# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
cluster_spec_1 = server_lib.ClusterSpec({
    "ps": [
        "ps0:2222",
        "ps1:2222"
    ]
})
cluster_spec_2 = server_lib.ClusterSpec({
    "worker": [
        "worker0:2222",
        "worker1:2222",
        "worker2:2222"
    ]
})
cluster_resolver_1 = SimpleClusterResolver(cluster_spec_1)
cluster_resolver_2 = SimpleClusterResolver(cluster_spec_2)

union_cluster = UnionClusterResolver(cluster_resolver_1, cluster_resolver_2)

unspecified_master = union_cluster.master()
self.assertEqual(unspecified_master, "")

specified_master = union_cluster.master("worker", 1)
self.assertEqual(specified_master, "worker1:2222")

rpc_master = union_cluster.master("worker", 1, rpc_layer="grpc")
self.assertEqual(rpc_master, "grpc://worker1:2222")
