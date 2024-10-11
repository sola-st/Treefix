# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
strategy = strategy_fn()
learning_rate = 2.
expected_gradient = resource_variable_ops.ResourceVariable(
    learning_rate / strategy.num_replicas_in_sync)
with strategy.scope():
    var = variables.Variable([5.0])
    opt = gradient_descent.GradientDescentOptimizer(learning_rate)
    loss_scale = loss_scale_module.DynamicLossScale(
        initial_loss_scale=2, increment_period=1, multiplier=2)
    opt = loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(
        opt, loss_scale)
    self.assertEqual(
        loss_scale.initial_loss_scale % strategy.num_replicas_in_sync, 0)

    run_fn = self._run_fn_with_grad_check(strategy, var, opt,
                                          expected_gradient)
    run_op = strategy.experimental_run(run_fn)
    self.evaluate(variables.global_variables_initializer())
    self._run_if_in_graph_mode(run_op)
    # The loss is the identity of the variable. Therefore the gradient is 1,
    # and so the variable will be init_val - grad * lr == 5 - 1 * 2 == 3
    self.assertAllClose([3.], self.evaluate(var))

    # Loss scale will be double, so the expected gradient is also doubled.
    self.evaluate(
        expected_gradient.assign(2 * learning_rate /
                                 strategy.num_replicas_in_sync))
    run_op = strategy.experimental_run(run_fn)
    self._run_if_in_graph_mode(run_op)
    # As before, the 2 is subtracted from the variable, making it's new value
    # 1.
    self.assertAllClose([1.], self.evaluate(var))
