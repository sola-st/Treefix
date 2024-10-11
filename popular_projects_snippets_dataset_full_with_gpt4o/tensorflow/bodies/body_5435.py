# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(2))
with strategy.scope():
    initializer = init_ops_v2.Constant([0, 1, 2, 3])
    # Shape is not explicitly specified.
    v1 = variables.Variable(
        initial_value=lambda: initializer(shape=(4,), dtype=dtypes.int64),
        dtype=dtypes.int64)
    # Dtype is not explicitly specified.
    v2 = variables.Variable(
        initial_value=lambda: initializer(shape=(4,), dtype=dtypes.int64),
        shape=(4,))
    # Neither shape nor dtype is explicitly specified.
    v3 = variables.Variable(
        initial_value=lambda: initializer(shape=(4,), dtype=dtypes.int64))

for v in [v1, v2, v3]:
    self.assertIsInstance(v, sharded_variable.ShardedVariable)
    self.assertLen(v.variables, 2)
    self.assertRegex(v.variables[0].device, "/job:ps/replica:0/task:0")
    self.assertRegex(v.variables[1].device, "/job:ps/replica:0/task:1")
    self.assertAllEqual(v.variables[0], [0, 1])
    self.assertAllEqual(v.variables[1], [2, 3])
