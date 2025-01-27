# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
var = variables.Variable([2.0])
opt = gradient_descent.GradientDescentOptimizer(1.0)
loss_scale = 10.
opt = loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(opt, loss_scale)
grad_check_fn = create_identity_with_grad_check_fn(loss_scale)
loss = grad_check_fn(var)
run_op = get_gradients(opt, loss, [var])
self.evaluate(variables.global_variables_initializer())
# This will cause an assertion to run, as
# create_identity_with_grad_check_fn added an assertion op.
self.evaluate(run_op)
