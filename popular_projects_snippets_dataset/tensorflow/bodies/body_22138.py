# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
with strategy_fn().scope() as strategy:
    var = variables.Variable([1.0, 2.0])
    # An SGD optimizer with momentum has slot variables.
    opt = momentum.MomentumOptimizer(1.0, momentum=1.)
    initial_loss_scale = 2.
    loss_scale = loss_scale_module.DynamicLossScale(
        initial_loss_scale=initial_loss_scale,
        increment_period=1,
        multiplier=4)
    opt = loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(
        opt, loss_scale)
    loss = lambda: var / strategy.num_replicas_in_sync
    run_fn = lambda: opt.minimize(loss, var_list=[var])
    run_op = strategy.experimental_run(run_fn)
    self.evaluate(variables.global_variables_initializer())
    self._run_if_in_graph_mode(run_op)
    # The momentum accumulator starts at 0 and the gradient is 1. The
    # accumulator is incremented by the gradient, so it is now 1. Then the
    # variable is subtracted by the accumulator, so the variable is subtracted
    # by 1.
    self.assertAllClose([0.0, 1.0], self.evaluate(var))
    self.assertEqual(self.evaluate(opt._loss_scale()), initial_loss_scale * 4)

    run_op = strategy.experimental_run(run_fn)
    self._run_if_in_graph_mode(run_op)
    # The momentum accumulator was 1 before this step and the gradient is 1.
    # The accumulator is incremented by the gradient, so it is now 2. Then the
    # variable is subtracted by the accumulator, so the variable is subtracted
    # by 2.
    self.assertAllClose([-2., -1.], self.evaluate(var))
    self.assertEqual(
        self.evaluate(opt._loss_scale()), initial_loss_scale * 16)
