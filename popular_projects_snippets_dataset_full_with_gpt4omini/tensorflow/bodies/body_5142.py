# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "chief": ["127.0.0.1:1234"],
    "worker": ["127.0.0.1:8964", "127.0.0.1:2333"],
    "evaluator": ["127.0.0.1:7566"]
}
self.assertEqual(
    multi_worker_util.worker_count(cluster_spec, task_type="evaluator"), 1)
