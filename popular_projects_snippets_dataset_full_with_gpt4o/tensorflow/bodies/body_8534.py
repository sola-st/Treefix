# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Create a local cluster with 2 workers."""
cls._cluster_spec = create_in_process_cluster(num_workers=num_workers,
                                              num_ps=num_ps)
cls._default_target = 'grpc://' + cls._cluster_spec['worker'][0]
