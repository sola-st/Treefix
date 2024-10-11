# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
spec = TwoTensorsSpec([5, 3], dtypes.int32, [None], dtypes.bool)
self.assertEqual(spec, trace_type.deserialize(trace_type.serialize(spec)))
