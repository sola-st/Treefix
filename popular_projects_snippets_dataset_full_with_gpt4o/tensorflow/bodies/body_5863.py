# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver_test.py
self.assertProtoEquals(expected_proto, cluster_spec.as_cluster_def())
self.assertProtoEquals(
    expected_proto, server_lib.ClusterSpec(cluster_spec).as_cluster_def())
self.assertProtoEquals(
    expected_proto,
    server_lib.ClusterSpec(cluster_spec.as_cluster_def()).as_cluster_def())
self.assertProtoEquals(
    expected_proto,
    server_lib.ClusterSpec(cluster_spec.as_dict()).as_cluster_def())
