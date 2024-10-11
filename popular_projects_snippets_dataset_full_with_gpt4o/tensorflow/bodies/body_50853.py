# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/tracing_utils_test.py
t = MyTrackable()
t._serialize_to_tensors = (def_function.function(t._serialize_to_tensors)
                           .get_concrete_function())
restored_tensor_spec = t._serialize_to_tensors.structured_outputs
# The wrapped tf.function doesn't matter.
t._restore_from_tensors = (def_function.function(lambda x: x)
                           .get_concrete_function(restored_tensor_spec))

save_fn, restore_fn = tracing_utils.trace_save_and_restore(t)
self.assertIs(t._serialize_to_tensors, save_fn)
self.assertIs(t._restore_from_tensors, restore_fn)
