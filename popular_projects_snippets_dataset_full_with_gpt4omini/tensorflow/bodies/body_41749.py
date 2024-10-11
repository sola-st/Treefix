# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
value = constant_op.constant(1.0)

@polymorphic_function.function
def lazy_capture(x):
    y = ops.get_default_graph().capture_call_time_value(
        lambda: value, tensor_spec.TensorSpec(()))
    exit(x + y)

self.assertAllEqual(lazy_capture(2.0), 3.0)

# dtype mismatch
value = constant_op.constant(1)
with self.assertRaisesRegex(ValueError, 'Value .* to a tensor with dtype'):
    lazy_capture(2.0)

# shape mismatch
value = constant_op.constant([1.0])
with self.assertRaisesRegex(ValueError, 'Value .* shape'):
    lazy_capture(2.0)
