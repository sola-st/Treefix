# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {}
with self.assertRaisesRegex(
    ValueError, "`task_type` 'worker' not found in cluster_spec."):
    multi_worker_util.worker_count(cluster_spec, task_type="worker")
