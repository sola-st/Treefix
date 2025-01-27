# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
cluster_def = multi_worker_test_base.create_cluster_spec(
    num_workers=0, num_ps=1, has_chief=True)
cluster_resolver = SimpleClusterResolver(
    ClusterSpec(cluster_def), rpc_layer="grpc", task_type="ps", task_id=0)
with self.assertRaisesRegexp(ValueError,
                             "There must be at least one worker."):
    parameter_server_strategy_v2.ParameterServerStrategyV2(cluster_resolver)
