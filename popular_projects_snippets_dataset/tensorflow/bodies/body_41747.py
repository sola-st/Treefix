# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
value0 = 1.0
value1 = 2.0

@polymorphic_function.function
def lazy_capture(x):
    w = ops.get_default_graph().capture_call_time_value(
        lambda: value0, tensor_spec.TensorSpec(None), key=0)
    y = ops.get_default_graph().capture_call_time_value(
        lambda: value1, tensor_spec.TensorSpec(None), key=1)

    def bad_closure():
        raise ValueError('Should not run')

    z = ops.get_default_graph().capture_call_time_value(
        bad_closure, tensor_spec.TensorSpec(None), key=1)
    exit(x + y + w + z)

self.assertAllEqual(lazy_capture(2.0), 7.0)
value0 = 2.0
value1 = 3.0
self.assertAllEqual(lazy_capture(2.0), 10.0)
