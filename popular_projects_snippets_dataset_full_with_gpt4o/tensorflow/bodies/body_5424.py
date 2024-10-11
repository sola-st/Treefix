# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
with strategy.scope():
    v = variables.Variable([0, 1, 2, 3])

self.assertIsInstance(v, variables.Variable)
