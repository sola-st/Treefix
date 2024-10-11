# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
super(BaseFaultToleranceTest, self).setUp()

self._cluster = multi_worker_test_base.create_multi_process_cluster(
    num_workers=num_workers, num_ps=num_ps, rpc_layer="grpc")
self._cluster_def = self._cluster.cluster_resolver.cluster_spec().as_dict()
self._cluster_def["chief"] = [
    "localhost:%d" % multi_worker_test_base.pick_unused_port()
]
cluster_resolver = SimpleClusterResolver(
    server_lib.ClusterSpec(self._cluster_def), rpc_layer="grpc")

# The strategy's constructor would connect to the cluster.
self.strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    cluster_resolver)
self.cluster_coord = cluster_coordinator.ClusterCoordinator(self.strategy)

self.thread_coord = thread_coordinator.Coordinator(
    clean_stop_exception_types=[])
self.num_workers = num_workers
self.num_ps = num_ps
