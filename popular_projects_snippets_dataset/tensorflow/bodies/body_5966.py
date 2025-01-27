# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
super(DistributedTableTest, cls).setUpClass()
cls.cluster = multi_worker_test_base.create_multi_process_cluster(
    num_workers=2, num_ps=3, rpc_layer="grpc")
cls.cluster_resolver = cls.cluster.cluster_resolver
