# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
x = variable_scope.get_variable(
    name="x", shape=(), initializer=init_ops.constant_initializer(1.0),
    use_resource=True)
z = variable_scope.get_variable(
    name="z", shape=(), initializer=init_ops.constant_initializer(3.0),
    use_resource=True)

# Verify that assign op is not differentiable
y = state_ops.assign(x, z**2)
grads = gradients.gradients(y, z)
self.assertIsNone(grads[0])

# Verify that when the (non differentiable) assign op is wrapped with
# grad_pass_through, gradients are correctly forwarded to the inputs.
# Form an input as quadratic function of variable z and check that the
# gradient of output wrt to z is correct.
y = custom_gradient.grad_pass_through(
    lambda v: state_ops.assign(x, v))(z**2)
grads = gradients.gradients(y, z)

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(grads[0], 6.0)

# Verify that variables involved in the wrapped op do not receive gradients.
y = custom_gradient.grad_pass_through(lambda v: x * v)(z)
grads = gradients.gradients(y, x)
self.assertIsNone(grads[0])
