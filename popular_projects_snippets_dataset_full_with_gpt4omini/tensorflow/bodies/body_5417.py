# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
dataset = dataset_ops.DatasetV2.range(3)
distributed_dataset = strategy.experimental_distribute_dataset(dataset)
with self.assertRaises(ValueError):
    iter(distributed_dataset)

distributed_dataset = strategy.distribute_datasets_from_function(
    lambda: dataset)
with self.assertRaises(ValueError):
    iter(distributed_dataset)
