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

def closure():
    exit(new_bool_captured_tensor)

concrete_fn.graph.replace_capture_with_deferred_capture(
    concrete_fn.captured_inputs[0],
    closure,
    spec=tensor_spec.TensorSpec(shape=(), dtype=dtypes.bool),
    placeholder=concrete_fn.inputs[1])

concrete_fn.set_external_captures([
    closure, concrete_fn._captured_inputs[1],
    concrete_fn._captured_inputs[2]
])
self.assertAllEqual(concrete_fn(), [5.])
