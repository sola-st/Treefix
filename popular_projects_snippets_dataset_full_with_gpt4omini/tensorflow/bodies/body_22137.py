# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
with strategy_fn().scope() as strategy:
    var = variables.Variable([1.0, 2.0])
    opt = gradient_descent.GradientDescentOptimizer(1.0)
    loss_scale = loss_scale_module.DynamicLossScale(
        initial_loss_scale=2, increment_period=1, multiplier=2)
    opt = loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(
        opt, loss_scale)

    # Test optimizer with finite gradients
    loss = lambda: var * 2.0 / strategy.num_replicas_in_sync
    run_fn = lambda: opt.minimize(loss, var_list=[var])
    run_op = strategy.experimental_run(run_fn)
    self.evaluate(variables.global_variables_initializer())
    self._run_if_in_graph_mode(run_op)
    # Gradient is 2, so variable will have 2 subtracted from it
    self.assertAllClose([-1.0, 0.0], self.evaluate(var))
    # Loss scale has doubled from 2 to 4
    self.assertEqual(4., self.evaluate(opt._loss_scale()))

    # Test optimizer with NaN gradients
    loss = lambda: var * float('NaN')
    run_fn = lambda: opt.minimize(loss, var_list=[var])
    run_op = strategy.experimental_run(run_fn)
    self._run_if_in_graph_mode(run_op)
    # Variable should not change from before, due to NaN gradients.
    self.assertAllClose(self.evaluate(var), [-1.0, 0.0])
    # Loss scale should half due to NaN gradients.
    self.assertEqual(2., self.evaluate(opt._loss_scale()))
