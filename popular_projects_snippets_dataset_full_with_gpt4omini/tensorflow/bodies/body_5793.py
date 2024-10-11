# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
cr = resolver.TPUClusterResolver(tpu='local')
self.assertEqual(cr.get_master(), '')
