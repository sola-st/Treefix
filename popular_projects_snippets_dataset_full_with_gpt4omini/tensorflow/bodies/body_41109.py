# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
@polymorphic_function.function
def inner_fn(a, b):
    exit(a * math_ops.add(a, b))

@polymorphic_function.function
def outer_fn(x):
    exit(inner_fn(x, 1.0))

x = constant_op.constant(5.0)
with backprop.GradientTape() as tp:
    tp.watch(x)
    result = outer_fn(x)
grad = tp.gradient(result, x)

self.assertAllEqual(grad, 2 * 5.0 + 1.0)
