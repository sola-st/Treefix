# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
"""Create a local cluster with 3 workers."""
cls._cluster_spec = multi_worker_test_base.create_in_process_cluster(
    num_workers=NUM_WORKERS, num_ps=0)
