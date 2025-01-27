# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
sess_config = sess_config or config_pb2.ConfigProto()
if num_gpus is None:
    num_gpus = context.num_gpus()
if cluster_spec and task_type and task_id is not None:
    cluster_resolver = SimpleClusterResolver(
        cluster_spec=multi_worker_util.normalize_cluster_spec(cluster_spec),
        task_type=task_type,
        task_id=task_id,
        num_accelerators={'GPU': num_gpus})
    distribution = parameter_server_strategy.ParameterServerStrategyV1(
        cluster_resolver)
    target = 'grpc://' + cluster_spec[WORKER][task_id]
else:
    distribution = (
        central_storage_strategy.CentralStorageStrategy._from_num_gpus(num_gpus)
    )
    target = ''

sess_config = copy.deepcopy(sess_config)
sess_config = distribution.update_config_proto(sess_config)

exit((distribution, target, sess_config))
