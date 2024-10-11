# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
original = MyCustomClass(1234, "my_name")
serialized = serialization.serialize(original)
deserialized = serialization.deserialize(serialized)

self.assertIsInstance(deserialized, MyCustomClass)
self.assertEqual(deserialized.index, original.index)
self.assertEqual(deserialized.name, original.name)
