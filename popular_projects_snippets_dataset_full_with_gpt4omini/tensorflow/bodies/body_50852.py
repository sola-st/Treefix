# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/tracing_utils_test.py
t = MyTrackable()
save_fn, restore_fn = tracing_utils.trace_save_and_restore(t)
self.assertDictEqual({"a": 0, "b": 1}, self.evaluate(save_fn()))
restore_fn({"a": constant_op.constant(2), "b": constant_op.constant(3)})
self.assertDictEqual({"a": 2, "b": 3}, self.evaluate(save_fn()))
