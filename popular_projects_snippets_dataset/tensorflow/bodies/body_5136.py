# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = server_lib.ClusterSpec({
    "chief": ["127.0.0.1:1234"],
    "worker": ["127.0.0.1:8964", "127.0.0.1:2333"],
    "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
})
self.assert_same_cluster(
    cluster_spec, multi_worker_util.normalize_cluster_spec(cluster_spec))
