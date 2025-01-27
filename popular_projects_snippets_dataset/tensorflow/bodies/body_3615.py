# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
original = MyCompositeClass(
    MyCustomClass(1, "name_1"), MyCustomClass(2, "name_2"),
    MyCustomClass(3, "name_3"))
serialized = serialization.serialize(original)
deserialized = serialization.deserialize(serialized)

self.assertIsInstance(deserialized, MyCompositeClass)

self.assertEqual(deserialized.elements[0].index, 1)
self.assertEqual(deserialized.elements[1].index, 2)
self.assertEqual(deserialized.elements[2].index, 3)

self.assertEqual(deserialized.elements[0].name, "name_1")
self.assertEqual(deserialized.elements[1].name, "name_2")
self.assertEqual(deserialized.elements[2].name, "name_3")
