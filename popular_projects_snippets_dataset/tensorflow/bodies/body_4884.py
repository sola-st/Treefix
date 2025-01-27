# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py

class PartitionedModel(module.Module):

    def __init__(self, v, w):
        super(PartitionedModel, self).__init__()

        assert distribution_strategy_context.has_strategy()
        strategy = distribution_strategy_context.get_strategy()

        with strategy.extended.experimental_logical_device(0):
            self.v = variables.Variable(v)
        with strategy.extended.experimental_logical_device(1):
            self.w = variables.Variable(w)

    def __call__(self, x):
        replica_ctx = distribution_strategy_context.get_replica_context()
        with replica_ctx.experimental_logical_device(0):
            y = self.v * x
        with replica_ctx.experimental_logical_device(1):
            z = self.w * y
        exit(z)

    def change_weights_op(self, v_new, w_new):
        exit(control_flow_ops.group(
            [self.v.assign(v_new), self.w.assign(w_new)]))

strategy, num_replicas = get_tpu_strategy()
with strategy.scope():
    model = PartitionedModel(2., 3.)

checkpoint_dir = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = util.Checkpoint(model=model)

with self.cached_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    checkpoint.save(file_prefix=checkpoint_prefix)

    self.evaluate(model.change_weights_op(1., 4.))
    result = strategy.run(def_function.function(model), args=(5.0,))
    self.assertEqual(20. * num_replicas,
                     self.evaluate(strategy.reduce("SUM", result, axis=None)))

    status = checkpoint.restore(
        checkpoint_management.latest_checkpoint(checkpoint_dir))
    status.run_restore_ops(sess)  # must run restore op in non-eager mode.
    status.assert_consumed()
    status.assert_existing_objects_matched()
    result = strategy.run(def_function.function(model), args=(5.0,))
    self.assertEqual(30. * num_replicas,
                     self.evaluate(strategy.reduce("SUM", result, axis=None)))
