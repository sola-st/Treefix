# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
super().setUp()

self._cluster = multi_worker_test_base.create_multi_process_cluster(
    num_workers=num_workers, num_ps=num_ps, rpc_layer="grpc")
self._cluster_def = self._cluster.cluster_resolver.cluster_spec().as_dict()
self._cluster_def["chief"] = [
    "localhost:%d" % multi_worker_test_base.pick_unused_port()
]
cluster_resolver = SimpleClusterResolver(
    server_lib.ClusterSpec(self._cluster_def), rpc_layer="grpc")

context.context().configure_coordination_service(
    service_type="standalone",
    service_leader="/job:ps/replica:0/task:0",
    heartbeat_timeout_in_ms=_PULL_FREQ_IN_SEC * 1000)
self.strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    cluster_resolver)
self.cluster_coord = cluster_coordinator.ClusterCoordinator(self.strategy)

self.num_workers = num_workers
self.num_ps = num_ps

self.states = None
self.polling_thread = RepeatedTimer(
    interval=_PULL_FREQ_IN_SEC, function=self.get_task_states)
