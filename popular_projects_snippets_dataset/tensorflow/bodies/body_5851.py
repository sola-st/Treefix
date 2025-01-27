# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
"""Verifies that the ClusterSpec generates the correct proto.

    We are testing this four different ways to ensure that the ClusterSpec
    returned by the TPUClusterResolver behaves identically to a normal
    ClusterSpec when passed into the generic ClusterSpec libraries.

    Args:
      cluster_spec: ClusterSpec returned by the TPUClusterResolver
      expected_proto: Expected protobuf
    """
self.assertProtoEquals(expected_proto, cluster_spec.as_cluster_def())
self.assertProtoEquals(
    expected_proto,
    server_lib.ClusterSpec(cluster_spec).as_cluster_def())
self.assertProtoEquals(expected_proto,
                       server_lib.ClusterSpec(
                           cluster_spec.as_cluster_def()).as_cluster_def())
self.assertProtoEquals(expected_proto,
                       server_lib.ClusterSpec(
                           cluster_spec.as_dict()).as_cluster_def())
