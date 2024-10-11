# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
cluster_spec = server_lib.ClusterSpec({
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": []
})

expected_proto = """
    job { name: 'ps' tasks { key: 0 value: 'ps0:2222' }
                     tasks { key: 1 value: 'ps1:2222' } }
    job { name: 'worker' }
    """

self.assertProtoEquals(expected_proto, cluster_spec.as_cluster_def())
self.assertProtoEquals(
    expected_proto, server_lib.ClusterSpec(cluster_spec).as_cluster_def())
self.assertProtoEquals(
    expected_proto,
    server_lib.ClusterSpec(cluster_spec.as_cluster_def()).as_cluster_def())
self.assertProtoEquals(
    expected_proto,
    server_lib.ClusterSpec(cluster_spec.as_dict()).as_cluster_def())
