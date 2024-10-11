# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "chief": ["127.0.0.1:1234"],
    "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
}
multi_worker_util._validate_cluster_spec(cluster_spec, "evaluator", 0)
with self.assertRaisesRegex(
    ValueError, "`task_type` 'worker' not found in cluster_spec."):
    multi_worker_util._validate_cluster_spec(cluster_spec, "worker", 0)
