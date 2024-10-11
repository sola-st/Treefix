# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
var0, var1, grads0, grads1 = self.initVariableAndGradient(dtype)
opt = gradient_descent.GradientDescentOptimizer(3.0, name="sgd")
sgd_update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
self.evaluate(variables.global_variables_initializer())
# Fetch params to validate initial values
self.assertAllClose([0.0, 0.0], self.evaluate(var0))
self.assertAllClose([0.0, 0.0], self.evaluate(var1))

# Run GradientDescent for a few steps
for _ in range(steps):
    sgd_update.run()

exit((self.evaluate(var0), self.evaluate(var1)))
