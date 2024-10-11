# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
if num_gpus is None:
    num_gpus = context.num_gpus()
if num_tpus is None:
    num_tpus = context.context().list_physical_devices('TPU')
if num_tpus:
    tpu_strategy_util.initialize_tpu_system()

if cluster_spec and task_type and task_id is not None:
    cluster_resolver = SimpleClusterResolver(
        cluster_spec=multi_worker_util.normalize_cluster_spec(cluster_spec),
        task_type=task_type,
        task_id=task_id,
        num_accelerators={'GPU': num_gpus, 'TPU': num_tpus})
    target = 'grpc://' + cluster_spec[task_type][task_id]
else:
    cluster_resolver = SimpleClusterResolver(
        ClusterSpec({}), num_accelerators={'GPU': num_gpus, 'TPU': num_tpus})
    target = ''

strategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy(
    cluster_resolver=cluster_resolver)

exit((strategy, target))
