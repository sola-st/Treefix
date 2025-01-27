# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
optimizer = adam.AdamOptimizer()

with context.eager_mode():
    var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")
    grads0 = constant_op.constant(np.array([0.1, 0.1]))
    optimizer.apply_gradients([(grads0, var0)])

g = ops.Graph()
with g.as_default():
    with session.Session():
        var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")
        grads0 = constant_op.constant(np.array([0.1, 0.1]))
        optimizer.apply_gradients([(grads0, var0)])

gg = ops.Graph()
with gg.as_default():
    with session.Session():
        var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")
        grads0 = constant_op.constant(np.array([0.1, 0.1]))

        # If the optimizer saves any state not keyed by graph the following line
        # fails.
        optimizer.apply_gradients([(grads0, var0)])
