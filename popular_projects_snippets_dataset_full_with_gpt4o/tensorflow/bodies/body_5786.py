# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
cluster_resolver = resolver.TPUClusterResolver(
    tpu='grpc://10.1.2.3:8470')
self.assertEqual(cluster_resolver.master(), 'grpc://10.1.2.3:8470')
