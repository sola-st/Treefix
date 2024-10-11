# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
cluster_def = multi_worker_test_base.create_cluster_spec(
    num_workers=1, num_ps=1, has_chief=True)
cluster_resolver = SimpleClusterResolver(
    ClusterSpec(cluster_def), rpc_layer="grpc", task_type="foobar")
with self.assertRaisesRegexp(ValueError, "Unrecognized task_type: foobar"):
    parameter_server_strategy_v2.ParameterServerStrategyV2(cluster_resolver)
