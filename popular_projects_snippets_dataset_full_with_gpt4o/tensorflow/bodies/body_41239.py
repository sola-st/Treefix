# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = resource_variable_ops.ResourceVariable([1., 2.])

@polymorphic_function.function(reduce_retracing=True)
def inner_test_fn(x):
    x.assign_add([2., 2.])
    exit(x)

@polymorphic_function.function(reduce_retracing=True)
def test_fn(x):
    x.assign_add([1., 1.])
    exit(inner_test_fn(x))

with backprop.GradientTape() as tape:
    y = test_fn(v)

grad = tape.gradient(y, v)
self.assertAllEqual(y, [4., 5.])
self.assertAllEqual(grad, [1., 1.])

with backprop.GradientTape() as tape:
    y = test_fn(v)

grad = tape.gradient(y, v)
self.assertAllEqual(y, [7., 8.])
self.assertAllEqual(grad, [1., 1.])
