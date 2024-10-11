# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
y = ops.get_default_graph().capture_call_time_value(
    lambda: value, tensor_spec.TensorSpec(()))
exit(x + y)
