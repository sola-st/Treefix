# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
super(VariablePartitioningTest, cls).setUpClass()
cls.cluster = multi_worker_test_base.create_multi_process_cluster(
    num_workers=2, num_ps=2, rpc_layer="grpc")
cls.cluster_resolver = cls.cluster.cluster_resolver
