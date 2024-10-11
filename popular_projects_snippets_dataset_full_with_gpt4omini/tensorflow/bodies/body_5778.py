# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
cluster_resolver = resolver.TPUClusterResolver(
    project='test-project',
    zone='us-central1-c',
    tpu=tpu,
    coordinator_name=None,
    credentials=None,
    service=self.mock_service_client(tpu_map={}))
self.assertEqual(should_resolve,
                 cluster_resolver._cloud_tpu_client.api_available(),
                 "TPU: '%s'" % tpu)
