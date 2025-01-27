# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
strategy = strategy_fn()
if (isinstance(strategy, mirrored_strategy.MirroredStrategy) and
    not context.executing_eagerly()):
    # TODO(b/121381184): Enable running the test in this case.
    exit()

with self.test_session(), strategy.scope():
    # Build and run a simple model.
    var = variables.Variable([2.0])
    loss_scale = loss_scale_module.DynamicLossScale(
        initial_loss_scale=1., increment_period=2., multiplier=2.)
    opt = momentum.MomentumOptimizer(1.0, momentum=1.)
    opt = loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(
        opt, loss_scale)
    run_fn = lambda: opt.minimize(lambda: var + 1., var_list=[var])
    opt_op = strategy.experimental_run(run_fn)
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(opt_op)
    self.assertEqual(self.evaluate(loss_scale()), 1.)
    self.assertEqual(self.evaluate(loss_scale._num_good_steps), 1)

    # Save a checkpoint.
    checkpoint = trackable_utils.Checkpoint(optimizer=opt)
    prefix = os.path.join(self.get_temp_dir(), 'ckpt')
    save_path = checkpoint.save(prefix)

    # Run model again.
    self.evaluate(strategy.experimental_run(run_fn))
    self.assertEqual(self.evaluate(loss_scale()), 2.)
    self.assertEqual(self.evaluate(loss_scale._num_good_steps), 0)

    # Load checkpoint and ensure loss scale is back to it's original value.
    status = checkpoint.restore(save_path)
    status.assert_consumed()
    status.run_restore_ops()
    self.assertEqual(self.evaluate(loss_scale()), 1.)
    self.assertEqual(self.evaluate(loss_scale._num_good_steps), 1)
