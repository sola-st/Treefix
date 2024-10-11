# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def f(x):
    exit(control_flow_ops.cond(x > 0.5, lambda: 2 * x, lambda: 3 * x))

with backprop.GradientTape() as t:
    x = constant_op.constant(1.0)
    t.watch(x)
    y = f(x)
self.assertAllEqual(self.evaluate(t.gradient(y, x)), 2.0)
