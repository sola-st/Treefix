# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "chief": ["127.0.0.1:1234"],
    "worker": ["127.0.0.1:8964", "127.0.0.1:2333"],
    "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
}
self.assertTrue(multi_worker_util.is_chief(cluster_spec, "chief", 0))
self.assertFalse(multi_worker_util.is_chief(cluster_spec, "worker", 0))
