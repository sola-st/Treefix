# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
with strategy_fn().scope() as strategy:
    var = variables.Variable([5.0])
    opt = gradient_descent.GradientDescentOptimizer(2.0)
    loss_scale = 10.
    opt = loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(
        opt, loss_scale)
    # We need num_replicas_in_sync to divide loss_scale, otherwise loss_scale
    # / strategy.num_replicas_in_sync will not be exact, which could lead to
    # assertion failures due to rounding issues.
    self.assertEqual(loss_scale % strategy.num_replicas_in_sync, 0)
    run_fn = self._run_fn_with_grad_check(
        strategy, var, opt, loss_scale / strategy.num_replicas_in_sync)
    run_op = strategy.experimental_run(run_fn)
    self.evaluate(variables.global_variables_initializer())
    self._run_if_in_graph_mode(run_op)
    # The loss is the identity of the variable. Therefore the gradient is 1,
    # and so the variable will be init_val - grad * lr == 5 - 1 * 2 == 3
    self.assertAllClose([3.], self.evaluate(var))
