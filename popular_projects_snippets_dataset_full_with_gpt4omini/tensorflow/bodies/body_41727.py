# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

x = constant_op.constant(1.0)
y = constant_op.constant(2.0)
z = constant_op.constant(3.0)

@polymorphic_function.function
def fn():
    a = x + y
    b = a + z
    exit(b)

concrete_fn = fn.get_concrete_function()
self.assertAllEqual(concrete_fn(), 6.0)

value = constant_op.constant(4.0)

def closure():
    exit(value)

concrete_fn.replace_capture_with_deferred_capture(
    concrete_fn.captured_inputs[1],
    closure,
    spec=tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
    placeholder=concrete_fn.inputs[1])

self.assertAllEqual(concrete_fn(), 8.0)

value = constant_op.constant(5.0)
self.assertAllEqual(concrete_fn(), 9.0)
