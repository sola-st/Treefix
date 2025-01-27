# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
self.assertEqual(trace_type.deserialize(trace_type.serialize(dtype)), dtype)
