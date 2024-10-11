# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def f(x):
    exit(control_flow_ops.while_loop(lambda _, i: i < 2,
                                       lambda x, i: (2*x, i + 1),
                                       [x, 0])[0])

with backprop.GradientTape() as t:
    x = constant_op.constant(1.0)
    t.watch(x)
    y = f(x)
self.assertAllEqual(self.evaluate(t.gradient(y, x)), 4.0)
