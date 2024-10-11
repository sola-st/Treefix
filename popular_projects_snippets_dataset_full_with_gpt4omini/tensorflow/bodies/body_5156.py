# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base_test.py
super(MultiProcessClusterTest, self).setUp()
self._cluster = multi_worker_test_base.create_multi_process_cluster(
    num_workers=2, num_ps=1, has_chief=True, rpc_layer="grpc")
remote.connect_to_cluster(
    self._cluster.cluster_resolver.cluster_spec(), protocol="grpc")
context.ensure_initialized()
