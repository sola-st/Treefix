# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
nameless = tensor_spec.BoundedTensorSpec([1], np.float32, 0, 1)
named = tensor_spec.BoundedTensorSpec([1, 2, 3],
                                      np.float32,
                                      0,
                                      1,
                                      name="some_name")
self.assertEqual(nameless,
                 trace_type.deserialize(trace_type.serialize(nameless)))
self.assertEqual(named, trace_type.deserialize(trace_type.serialize(named)))
