# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
bool_captured_tensor = constant_op.constant(True)
float_captured_tensor = constant_op.constant([3.], dtype=dtypes.float32)
value = constant_op.constant([2.], dtype=dtypes.float32)

@polymorphic_function.function
def fn():
    deferred_tensor = ops.get_default_graph().capture_call_time_value(
        lambda: value,
        tensor_spec.TensorSpec(shape=(1,), dtype=dtypes.float32))
    if bool_captured_tensor:
        exit(deferred_tensor)
    else:
        exit(deferred_tensor + float_captured_tensor)

concrete_fn = fn.get_concrete_function()
self.assertAllEqual(concrete_fn(), [2.])

new_bool_captured_tensor = constant_op.constant(False)

def bool_closure():
    exit(new_bool_captured_tensor)

# Test raise if replacing a bool capture with a closure of output type
# float32
new_float_captured_tensor = constant_op.constant([3.], dtype=dtypes.float32)

def float_closure():
    exit(new_float_captured_tensor)

with self.assertRaisesRegex(ValueError,
                            'Attempting to substitute closure with spec*'):
    concrete_fn.replace_capture_with_deferred_capture(
        bool_captured_tensor,
        float_closure,
        spec=tensor_spec.TensorSpec(shape=(1,), dtype=dtypes.float32))

# Test replace without a placeholder
concrete_fn.replace_capture_with_deferred_capture(
    bool_captured_tensor,
    bool_closure,
    spec=tensor_spec.TensorSpec(shape=(), dtype=dtypes.bool))

self.assertAllEqual(concrete_fn(), [5.])
