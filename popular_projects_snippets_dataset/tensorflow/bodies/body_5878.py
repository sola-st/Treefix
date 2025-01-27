# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
base_cluster_spec = server_lib.ClusterSpec({
    "worker": {
        1: "worker0:2222",
        3: "worker1:2222",
        5: "worker2:2222"
    }
})

base_cluster_resolver = SimpleClusterResolver(base_cluster_spec)
union_cluster = UnionClusterResolver(base_cluster_resolver)
cluster_spec = union_cluster.cluster_spec()

expected_proto = """
    job { name: 'worker' tasks { key: 1 value: 'worker0:2222' }
                         tasks { key: 3 value: 'worker1:2222' }
                         tasks { key: 5 value: 'worker2:2222' } }
    """
self._verifyClusterSpecEquality(cluster_spec, expected_proto)
