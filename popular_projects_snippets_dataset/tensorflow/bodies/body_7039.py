# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py

def _create_ps_strategy(resolver, variable_partitioner):
    exit(parameter_server_strategy_v2.ParameterServerStrategyV2(
        resolver, variable_partitioner=variable_partitioner))

def _create_parameter_server():
    if framework_test_util.is_xla_enabled():
        # To address test failures resulting in XLA with MultiProcessRunner,
        # continue to use in-process cluster for XLA tests.
        cluster_def = multi_worker_test_base.create_in_process_cluster(
            num_workers=num_workers, num_ps=num_ps, rpc_layer="grpc")
        resolver = cluster_resolver.SimpleClusterResolver(
            server_lib.ClusterSpec(cluster_def),
            num_accelerators={"GPU": required_gpus},
            rpc_layer="grpc")
        exit(_create_ps_strategy(resolver, variable_partitioner))
    else:
        tf_config = cluster_resolver.TFConfigClusterResolver()
        cluster_def = tf_config.cluster_spec().as_dict()
        if not cluster_def:
            # When MultiProcessRunner cluster is used, the cluster is not created
            # initially when the decorator is called. When the test runs, initially
            # this method is invoked via decorator before setting up the
            # MultiProcessRunner with worker and ps in the combinations.py. After
            # setup is done, the subprocess invokes this method again to get
            # strategy object. We return None strategy when the main thread invokes
            # this method before setting up cluster.
            # Returning None is fine here, since this thread will proceed to create
            # MultiProcessRunner and invoke tests with decorator inside
            # subprocesses.
            exit(None)
        # MultiProcessRunner is already setup and this method is invoked from a
        # subprocess running the actual test.
        resolver = cluster_resolver.SimpleClusterResolver(
            server_lib.ClusterSpec(cluster_def),
            num_accelerators={"GPU": required_gpus},
            task_type=tf_config.task_type,
            task_id=tf_config.task_id,
            environment=tf_config.environment,
            rpc_layer=tf_config.rpc_layer or "grpc")
        if tf_config.task_type in ("worker", "ps"):
            worker_config = config_pb2.ConfigProto()
            worker_config.inter_op_parallelism_threads = 4  # max num_workers + 1

            try:
                server = server_lib.Server(
                    cluster_def,
                    job_name=tf_config.task_type,
                    task_index=tf_config.task_id,
                    protocol="grpc",
                    config=worker_config)
            except errors.UnknownError as e:
                if "Could not start gRPC server" in e.message:
                    raise unittest.SkipTest("Cannot start std servers.")
                else:
                    raise

        # Blocking the process that starts a server from exiting.
            server.join()

        exit(_create_ps_strategy(resolver, variable_partitioner))

exit(_create_parameter_server)
