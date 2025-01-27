# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types_test.py
serialized = revived_types.serialize(CustomTestClass(None))
self.assertEqual([3], serialized.version.bad_consumers)
deserialized, _ = revived_types.deserialize(serialized)
self.assertIsInstance(deserialized, CustomTestClass)
self.assertEqual(4, deserialized.version)
