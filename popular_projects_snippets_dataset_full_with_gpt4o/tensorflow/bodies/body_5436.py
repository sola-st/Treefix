# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, lambda shape, dtype: None)
with self.assertRaisesRegex(ValueError, "variable_partitioner"):
    with strategy.scope():
        variables.Variable([[[0, 1], [2, 3]], [[0, 1], [2, 3]]])

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, lambda shape, dtype: [])
with self.assertRaisesRegex(ValueError, "variable_partitioner"):
    with strategy.scope():
        variables.Variable([[[0, 1], [2, 3]], [[0, 1], [2, 3]]])

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, lambda shape, dtype: [0, 1, 1])
with self.assertRaisesRegex(ValueError, "variable_partitioner"):
    with strategy.scope():
        variables.Variable([[[0, 1], [2, 3]], [[0, 1], [2, 3]]])

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, lambda shape, dtype: [2, 2, 1])
with self.assertRaisesRegex(ValueError, "variable_partitioner"):
    with strategy.scope():
        variables.Variable([[[0, 1], [2, 3]], [[0, 1], [2, 3]]])
