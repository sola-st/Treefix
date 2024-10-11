# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
cluster_resolver = resolver.TPUClusterResolver(tpu='grpc://10.1.2.3:8470')
self.assertEqual('grpc://10.1.2.3:8470', cluster_resolver.master())
self.assertEqual(
    server_lib.ClusterSpec({
        'worker': ['10.1.2.3:8470']
    }).as_dict(),
    cluster_resolver.cluster_spec().as_dict())
