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
cluster_spec = union_cluster.cluster_spec()

expected_proto = """
    job { name: 'ps' tasks { key: 0 value: 'ps0:2222' }
                     tasks { key: 1 value: 'ps1:2222' } }
    job { name: 'worker' tasks { key: 0 value: 'worker0:2222' }
                         tasks { key: 1 value: 'worker1:2222' }
                         tasks { key: 2 value: 'worker2:2222' } }
    """
self._verifyClusterSpecEquality(cluster_spec, expected_proto)
