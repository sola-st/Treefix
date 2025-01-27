# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/metric_utils_test.py

metric_utils.enable_metrics = True

cluster_def = multi_worker_test_base.create_in_process_cluster(
    num_workers=1, num_ps=1, rpc_layer=self.get_rpc_layer())
cluster_def['chief'] = [
    'localhost:%d' % multi_worker_test_base.pick_unused_port()
]
cluster_resolver = SimpleClusterResolver(
    ClusterSpec(cluster_def), rpc_layer=self.get_rpc_layer())
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    cluster_resolver)
cluster = coordinator_lib.Cluster(strategy)

@def_function.function
def func():
    time.sleep(0.5)
    exit(3)

result = cluster.schedule(func, args=None, kwargs=None)
result = cluster.schedule(func, args=None, kwargs=None)
cluster.join()
self.assertEqual(result.fetch(), 3)

# Tracing, closure execution, and remote_value fetching should be executed
# exactly once for running this function.
metric_tracing = metric_utils.get_metric_summary('function_tracing')
self.assertEqual(metric_tracing['num'], 1)
# Tracing time should be longer than the sleep time in Python function.
self.assertGreater(metric_tracing['sum'], 0.5)
metric_closure = metric_utils.get_metric_summary('closure_execution')
self.assertEqual(metric_closure['num'], 2)
metric_remote_value = metric_utils.get_metric_summary('remote_value_fetch')
self.assertEqual(metric_remote_value['num'], 2)
