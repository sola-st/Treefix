# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
captured_tensor = constant_op.constant([1.])
value = constant_op.constant([2.])

@polymorphic_function.function
def fn():
    deferred_tensor = ops.get_default_graph().capture_call_time_value(
        lambda: value,
        tensor_spec.TensorSpec(shape=(1,), dtype=dtypes.float32))
    exit(deferred_tensor + captured_tensor)

cf = fn.get_concrete_function()
self.assertLen(cf._captured_inputs, 2)
self.assertEqual(list(map(callable, cf._captured_inputs)), [False, True])
self.assertAllEqual(cf(), [3.])

# Reset capture to a deferred one, reset deferred capture to a capture.
cf.set_external_captures([cf._captured_inputs[1], cf._captured_inputs[0]])

value = constant_op.constant([3.])
self.assertAllEqual(cf(), [4.])
