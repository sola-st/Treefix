# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
cluster_def = multi_worker_test_base.create_cluster_spec(
    num_workers=1, num_ps=1, has_chief=True)
cluster_def["some_arbitrary_name"] = [
    "localhost:%d" % multi_worker_test_base.pick_unused_port()
]
cluster_resolver = SimpleClusterResolver(
    ClusterSpec(cluster_def), rpc_layer="grpc")
with self.assertRaisesRegexp(ValueError, "Disallowed task type found in"):
    parameter_server_strategy_v2.ParameterServerStrategyV2(cluster_resolver)
