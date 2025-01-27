# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
if test_util.is_xla_enabled():
    self.skipTest("TODO(b/202760274): Would raise an error that is to be "
                  "investigated.")

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(2))

collection = []

@def_function.function
def create_vars():
    if not collection:
        identity = init_ops_v2.Identity()
        v1 = variables.Variable([[1., 0.], [0., 1.]], dtype=dtypes.float32)
        v2 = variables.Variable(lambda: identity((2, 2), dtypes.float32))
        v3 = variables.Variable(
            lambda: identity((2, 2), dtypes.float32),
            dtype=dtypes.float32,
            shape=(2, 2))
        collection.extend([v1, v2, v3])

with strategy.scope():
    create_vars()
    for v in collection:
        self.assertIsInstance(v, sharded_variable.ShardedVariable)
        self.assertLen(v.variables, 2)
        self.assertRegex(v.variables[0].device, "/job:ps/replica:0/task:0")
        self.assertRegex(v.variables[1].device, "/job:ps/replica:0/task:1")
        self.assertAllEqual(v.variables[0], [[1., 0.]])
        self.assertAllEqual(v.variables[1], [[0., 1.]])
