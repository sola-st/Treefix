# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
cluster_def = multi_worker_test_base.create_cluster_spec(
    num_workers=1, num_ps=1)
chief_ports = [multi_worker_test_base.pick_unused_port() for _ in range(3)]
cluster_def["chief"] = ["localhost:%s" % port for port in chief_ports]
cluster_resolver = SimpleClusterResolver(
    ClusterSpec(cluster_def),
    rpc_layer="grpc",
    task_type="chief",
    task_id=1)
with self.assertRaisesRegexp(ValueError,
                             "There must be at most one 'chief' job."):
    parameter_server_strategy_v2.ParameterServerStrategyV2(cluster_resolver)
