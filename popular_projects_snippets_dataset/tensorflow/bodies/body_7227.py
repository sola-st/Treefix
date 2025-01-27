# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
cluster_spec = server_lib.ClusterSpec({
    "worker": ["/job:worker/task:0", "/job:worker/task:1"]
})
distribution.configure(cluster_spec=cluster_spec)
