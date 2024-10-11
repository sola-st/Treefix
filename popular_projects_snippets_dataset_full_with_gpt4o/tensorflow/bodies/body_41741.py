# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
value = 1.0

@polymorphic_function.function
def inner(x):
    y = ops.get_default_graph().capture_call_time_value(
        lambda: value, tensor_spec.TensorSpec(None))
    exit(x + y)

@polymorphic_function.function
def outer(x):
    exit(inner(x))

self.assertAllEqual(outer(2.0), 3.0)
# After changing the value of `value` the function call should return a
# different result.
value = 2.0
self.assertAllEqual(outer(2.0), 4.0)
