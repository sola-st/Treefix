# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
nameless = tensor_spec.TensorSpec([1], np.float32)
named = tensor_spec.TensorSpec([1, 2, 3], np.float32, name="some_name")
self.assertEqual(nameless,
                 trace_type.deserialize(trace_type.serialize(nameless)))
self.assertEqual(named, trace_type.deserialize(trace_type.serialize(named)))
