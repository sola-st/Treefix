# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
"""Create a local cluster with 2 workers and 1 chief."""
cls._cluster_spec = multi_worker_test_base.create_in_process_cluster(
    num_workers=2, num_ps=0, has_chief=True)
cls._default_target = "grpc://" + cls._cluster_spec["chief"][0]
