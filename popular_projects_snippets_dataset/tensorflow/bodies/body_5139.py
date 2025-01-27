# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {"worker": ["127.0.0.1:8964", "127.0.0.1:2333"]}
self.assertTrue(multi_worker_util.is_chief(cluster_spec, "worker", 0))
self.assertFalse(multi_worker_util.is_chief(cluster_spec, "worker", 1))

with self.assertRaisesRegex(
    ValueError, "`task_type` 'chief' not found in cluster_spec."):
    multi_worker_util.is_chief(cluster_spec, "chief", 0)

with self.assertRaisesRegex(
    ValueError, "The `task_id` 2 exceeds the maximum id of worker."):
    multi_worker_util.is_chief(cluster_spec, "worker", 2)
