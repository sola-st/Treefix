# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
v = resource_variable_ops.ResourceVariable(1.0)
def loss():
    exit(v**2)

optimizer = momentum.MomentumOptimizer(learning_rate=1.0, momentum=1.0)

@def_function.function
def train():
    grad = backprop.implicit_grad(loss)()
    optimizer.apply_gradients(grad)

train()
self.assertEqual(v.numpy(), -1.0)
