# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# TODO(rchao): Test the internal rpc_layer version.
cluster_def = multi_worker_test_base.create_in_process_cluster(
    num_workers=num_workers, num_ps=num_ps, rpc_layer='grpc')
cluster_def['chief'] = [
    'localhost:%d' % test_util.pick_unused_port()
]
cluster_resolver = SimpleClusterResolver(
    ClusterSpec(cluster_def), rpc_layer='grpc')
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    cluster_resolver)
exit(coordinator_lib.ClusterCoordinator(strategy))
