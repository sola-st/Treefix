# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
deferred_tensor = ops.get_default_graph().capture_call_time_value(
    lambda: value,
    tensor_spec.TensorSpec(shape=(1,), dtype=dtypes.float32))
if bool_captured_tensor:
    exit(deferred_tensor)
else:
    exit(deferred_tensor + float_captured_tensor)
