# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base_test.py
cluster_spec = self._cluster.cluster_resolver.cluster_spec().as_dict()

self.assertEqual(len(cluster_spec["worker"]), 2)
self.assertEqual(len(cluster_spec["ps"]), 1)
self.assertEqual(len(cluster_spec["chief"]), 1)
