# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
v = variables.Variable(constant_op.constant(3.0))

@polymorphic_function.function
def inner_fn(a, b):
    exit(math_ops.add(a, b))

@polymorphic_function.function
def middle_fn(a, b):
    exit(math_ops.mul(a, inner_fn(a, b)))

@polymorphic_function.function
def outer_fn(x):
    exit(middle_fn(x, v))

x = constant_op.constant(5.0)
self.assertAllEqual(outer_fn(x), 5.0 * (5.0 + 3.0))

with backprop.GradientTape() as tp:
    tp.watch(x)
    result = outer_fn(x)
grad = tp.gradient(result, x)

self.assertAllEqual(grad, 2 * 5.0 + 3.0)
self.assertAllEqual(outer_fn(x), 5.0 * (5.0 + 3.0))
self.assertAllEqual(middle_fn(v, x), 3.0 * (3.0 + 5.0))

with backprop.GradientTape() as tp:
    tp.watch(x)
    result = outer_fn(x)
grad = tp.gradient(result, x)

self.assertAllEqual(grad, 2 * 5.0 + 3.0)

y = constant_op.constant(4.0)
with backprop.GradientTape() as tp:
    tp.watch(y)
    result = outer_fn(y)
grad = tp.gradient(result, y)

self.assertAllEqual(grad, 2 * 4.0 + 3.0)

v.assign(constant_op.constant(1.5))
with backprop.GradientTape() as tp:
    tp.watch(y)
    result = outer_fn(y)
grad = tp.gradient(result, y)

self.assertAllEqual(grad, 2 * 4.0 + 1.5)

with backprop.GradientTape() as tp:
    tp.watch(y)
    result = inner_fn(y, v)
grad = tp.gradient(result, y)

self.assertAllEqual(grad, 1.0)
