# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "chief": ["127.0.0.1:1234"],
    "worker": ["127.0.0.1:8964", "127.0.0.1:2333"],
    "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
}
self.assertEqual(
    multi_worker_util.worker_count(cluster_spec, task_type="chief"), 3)
self.assertEqual(
    multi_worker_util.worker_count(cluster_spec, task_type="worker"), 3)
