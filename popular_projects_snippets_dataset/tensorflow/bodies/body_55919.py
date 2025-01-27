# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
def loss(v):
    exit(v**2)

optimizer = adam.AdamOptimizer(learning_rate=1.0)

@def_function.function
def train():
    grad = backprop.implicit_grad(loss)(self.v)
    optimizer.apply_gradients(grad)
    exit(self.v.read_value())

self.v = resource_variable_ops.ResourceVariable(1.0)
train()
