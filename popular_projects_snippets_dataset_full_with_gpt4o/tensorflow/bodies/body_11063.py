# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
x = variables.Variable(1.0, name="x")
z = variables.Variable(3.0, name="z")

# Verify that assign op is not differentiable
with backprop.GradientTape() as tape:
    y = x.assign(z**2)
grads = tape.gradient(y, z)
self.assertIsNone(grads)

# Verify that when the (non differentiable) assign op is wrapped with
# grad_pass_through, gradients are correctly forwarded to the inputs.
# Form an input as quadratic function of variable z and check that the
# gradient of output wrt to z is correct.
with backprop.GradientTape() as tape:
    y = custom_gradient.grad_pass_through(x.assign)(z**2)
grads = tape.gradient(y, z)
self.assertAllClose(grads, 6.0)

# Verify that variables involved in the wrapped op do not receive gradients.
with backprop.GradientTape() as tape:
    y = custom_gradient.grad_pass_through(lambda v: x * v)(z)
grads = tape.gradient(y, x)
self.assertIsNone(grads)
