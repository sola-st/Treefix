# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py
enable_collective_ops(cluster_resolver_lib.TFConfigClusterResolver())
context.context().check_collective_ops_peer_health(
    "localhost:12345", timeout_in_ms=1000)
