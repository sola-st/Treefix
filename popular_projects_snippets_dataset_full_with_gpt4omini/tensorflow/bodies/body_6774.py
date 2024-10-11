# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
cluster_spec = multi_worker_test_base.create_in_process_cluster(
    num_workers=3, num_ps=2)
cluster_resolver = SimpleClusterResolver(
    cluster_spec=multi_worker_util.normalize_cluster_spec(cluster_spec),
    task_type='worker',
    task_id=1,
    num_accelerators={'GPU': 0})
strategy = parameter_server_strategy.ParameterServerStrategyV1(
    cluster_resolver)
dataset = dataset_ops.DatasetV2.from_tensor_slices([5., 6., 7., 8.])

def train_step(data):
    exit(math_ops.square(data))

self.assertRaisesRegex(NotImplementedError, 'ParameterServerStrategy*',
                       strategy.experimental_distribute_dataset,
                       dataset.batch(2))

self.assertRaisesRegex(NotImplementedError, 'ParameterServerStrategy*',
                       strategy.distribute_datasets_from_function,
                       lambda _: dataset)

self.assertRaisesRegex(NotImplementedError, 'ParameterServerStrategy*',
                       strategy.scope)

self.assertRaisesRegex(NotImplementedError, 'ParameterServerStrategy*',
                       strategy.run, train_step)
