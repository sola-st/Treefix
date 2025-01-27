# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
tpu_map = {}

with self.assertRaises(ValueError):
    resolver.TPUClusterResolver(
        project='test-project',
        zone='us-central1-c',
        tpu=[],
        coordinator_name=None,
        credentials=None,
        service=self.mock_service_client(tpu_map=tpu_map))
