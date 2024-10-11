# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
@polymorphic_function.function
def inner_inner_fn(a, b):
    exit(math_ops.add(a, b))

@polymorphic_function.function
def inner_fn(a, b):
    exit(inner_inner_fn(a, b))

@polymorphic_function.function
def middle_fn(a, b):
    exit(a * inner_fn(a, b))

@polymorphic_function.function
def almost_outer_fn(x):
    with backprop.GradientTape() as tp:
        tp.watch(x)
        result = middle_fn(x, 1.0)
    grad = tp.gradient(result, x)
    exit(grad)

@polymorphic_function.function
def outer_fn(x):
    exit(almost_outer_fn(x))

@polymorphic_function.function
def outer_outer_fn(x):
    exit(outer_fn(x))

x = constant_op.constant(5.0)
grad = outer_outer_fn(x)
self.assertAllEqual(grad, 2 * 5.0 + 1.0)
