# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
var0, var1, grads0, grads1 = self.initVariableAndGradient(dtype)
opt = ftrl.FtrlOptimizer(
    3.0,
    learning_rate_power=-0.5,  # using Adagrad learning rate
    initial_accumulator_value=0.1,
    l1_regularization_strength=0.0,
    l2_regularization_strength=0.0)
ftrl_update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
self.evaluate(variables.global_variables_initializer())
# Fetch params to validate initial values
self.assertAllClose([0.0, 0.0], self.evaluate(var0))
self.assertAllClose([0.0, 0.0], self.evaluate(var1))

# Run Ftrl for a few steps
for _ in range(steps):
    ftrl_update.run()

exit((self.evaluate(var0), self.evaluate(var1)))
