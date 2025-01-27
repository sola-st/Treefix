# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(2))
with strategy.scope():
    init1 = init_ops_v2.Constant([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v1 = variables.Variable(
        initial_value=lambda: init1(shape=(5, 2), dtype=dtypes.int64),
        shape=(5, 2),
        dtype=dtypes.int64)

    init2 = init_ops_v2.Constant([0, 1, 2, 3, 4, 5])
    v2 = variables.Variable(
        initial_value=lambda: init2(shape=(6, 1), dtype=dtypes.int64),
        shape=(6, 1),
        dtype=dtypes.int64)

self.assertIsInstance(v1, sharded_variable.ShardedVariable)
self.assertLen(v1.variables, 2)
self.assertRegex(v1.variables[0].device, "/job:ps/replica:0/task:0")
self.assertRegex(v1.variables[1].device, "/job:ps/replica:0/task:1")
self.assertAllEqual(v1.variables[0], [[0, 1], [2, 3], [4, 5]])
self.assertAllEqual(v1.variables[1], [[6, 7], [8, 9]])

self.assertIsInstance(v2, sharded_variable.ShardedVariable)
self.assertLen(v2.variables, 2)
self.assertRegex(v2.variables[0].device, "/job:ps/replica:0/task:0")
self.assertRegex(v2.variables[1].device, "/job:ps/replica:0/task:1")
self.assertAllEqual(v2.variables[0], [[0], [1], [2]])
self.assertAllEqual(v2.variables[1], [[3], [4], [5]])
