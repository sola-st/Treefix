# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
os.environ['KUBE_GOOGLE_CLOUD_TPU_ENDPOINTS'] = ('grpc://10.120.27.5:8470,'
                                                 'grpc://10.120.27.6:8470,'
                                                 'grpc://10.120.27.7:8470,'
                                                 'grpc://10.120.27.8:8470')

self.assertIn('KUBE_GOOGLE_CLOUD_TPU_ENDPOINTS', os.environ)
cluster_resolver = resolver.TPUClusterResolver()
self.assertEqual(
    compat.as_bytes('grpc://10.120.27.5:8470'),
    compat.as_bytes(cluster_resolver.master()))
actual_cluster_spec = cluster_resolver.cluster_spec()
expected_proto = """
    job {
      name: 'worker'
      tasks { key: 0 value: '10.120.27.5:8470' }
      tasks { key: 1 value: '10.120.27.6:8470' }
      tasks { key: 2 value: '10.120.27.7:8470' }
      tasks { key: 3 value: '10.120.27.8:8470' }
    }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)

del os.environ['KUBE_GOOGLE_CLOUD_TPU_ENDPOINTS']
