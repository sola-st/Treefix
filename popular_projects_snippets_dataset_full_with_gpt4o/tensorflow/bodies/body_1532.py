# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/proximal_gradient_descent_test.py
var0 = resource_variable_ops.ResourceVariable([1.0, 2.0])
var1 = resource_variable_ops.ResourceVariable([3.0, 4.0])
grads0 = constant_op.constant([0.1, 0.2])
grads1 = constant_op.constant([0.01, 0.02])

update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
self.evaluate(variables.global_variables_initializer())

self.assertAllClose([1.0, 2.0], self.evaluate(var0))
self.assertAllClose([3.0, 4.0], self.evaluate(var1))

# Run ProximalAdagrad for a few steps
for _ in range(steps):
    update.run()

exit((self.evaluate(var0), self.evaluate(var1)))
