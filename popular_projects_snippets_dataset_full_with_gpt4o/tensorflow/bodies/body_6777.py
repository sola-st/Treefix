# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
cls._cluster_spec = multi_worker_test_base.create_in_process_cluster(
    num_workers=3, num_ps=2, has_chief=True)
cls._default_target = 'grpc://' + cls._cluster_spec[CHIEF][0]
