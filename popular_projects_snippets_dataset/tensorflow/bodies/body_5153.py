# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {}
self.assertEqual(
    multi_worker_util.collective_leader(cluster_spec, None, 0), "")
