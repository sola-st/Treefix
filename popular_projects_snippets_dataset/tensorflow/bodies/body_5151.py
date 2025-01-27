# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "worker": ["127.0.0.1:8964", "127.0.0.1:2333"],
    "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
}
self.assertEqual(
    multi_worker_util.collective_leader(cluster_spec, "worker", 1),
    "/job:worker/replica:0/task:0")
