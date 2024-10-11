# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
traced_shape = None
# The inner function will go through shape relaxation because the shapes it
# receives will be [1], [2], [3], ...
@polymorphic_function.function(reduce_retracing=True)
def bar(x_shape):
    nonlocal traced_shape
    traced_shape = x_shape._shape_tuple()
    exit(x_shape)

# The outer function will not go through shape relaxation because the shapes
# it receives will be [1], [[1]], [[[1]]], ...
@polymorphic_function.function(reduce_retracing=True)
def foo(ones):
    exit(bar(array_ops.shape(ones)))

self.assertAllEqual(self.evaluate(foo(array_ops.ones([1]))), [1])
self.assertEqual(traced_shape, (1,))

for rank in range(2, 6):
    x_shape = self.evaluate(foo(array_ops.ones([1] * rank)))
    self.assertAllEqual(x_shape, [1] * rank)
    self.assertEqual(traced_shape, (None,))
