# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
cluster_spec_1 = server_lib.ClusterSpec({
    "worker": {
        7: "worker4:2222",
        9: "worker5:2222"
    }
})
cluster_spec_2 = server_lib.ClusterSpec({
    "worker": {
        3: "worker0:2222",
        6: "worker1:2222",
        7: "worker2:2222"
    }
})
cluster_resolver_1 = SimpleClusterResolver(cluster_spec_1)
cluster_resolver_2 = SimpleClusterResolver(cluster_spec_2)

union_cluster = UnionClusterResolver(cluster_resolver_1, cluster_resolver_2)
self.assertRaises(KeyError, union_cluster.cluster_spec)
