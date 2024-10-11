# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
"""Create a local cluster with 3 workers."""
cls._cluster_spec = multi_worker_test_base.create_in_process_cluster(
    num_workers=3, num_ps=0)
