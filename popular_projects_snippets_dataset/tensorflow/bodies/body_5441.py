# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py

if test_util.is_xla_enabled() and not delayed and restore_shards == 4:
    self.skipTest("TODO(b/202760274): Would raise an error that is to be "
                  "investigated.")

def make_variable(name, shape, dtype, initializer):
    initial_value = functools.partial(initializer, shape, dtype=dtype)
    exit(variables.Variable(
        name=name, initial_value=initial_value, shape=shape, dtype=dtype))

class Model(autotrackable.AutoTrackable):

    def build(self):
        self.w = self._add_variable_with_custom_getter(
            "w",
            shape=(4,),
            initializer=init_ops_v2.Ones(),
            getter=make_variable)

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(2))
ckpt_dir = os.path.join(self.get_temp_dir(), "checkpoint")

with strategy.scope():
    model1 = Model()
    model1.build()
    self.assertIsInstance(model1.w, sharded_variable.ShardedVariable)
    self.assertLen(model1.w.variables, 2)
    model1.w.assign([1., 2., 3., 4.])

    cp1 = tracking_util.Checkpoint(model=model1)
    cp1.write(ckpt_dir)

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver,
    sharded_variable.FixedShardsPartitioner(restore_shards))

with strategy.scope():
    model2 = Model()
    cp2 = tracking_util.Checkpoint(model=model2)
    if delayed:
        cp2.restore(ckpt_dir)
        model2.build()
    else:
        model2.build()
        cp2.restore(ckpt_dir)
    self.assertIsInstance(model2.w, sharded_variable.ShardedVariable)
    self.assertLen(model2.w.variables, restore_shards)
    if restore_shards == 2:
        self.assertAllEqual(model2.w.variables[0], [1., 2.])
        self.assertAllEqual(model2.w.variables[1], [3., 4.])
    elif restore_shards == 4:
        self.assertAllEqual(model2.w.variables[0], [1.])
        self.assertAllEqual(model2.w.variables[1], [2.])
        self.assertAllEqual(model2.w.variables[2], [3.])
        self.assertAllEqual(model2.w.variables[3], [4.])
