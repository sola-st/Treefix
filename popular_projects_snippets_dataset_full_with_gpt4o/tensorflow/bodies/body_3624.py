# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
self.assertEqual(
    serialization.deserialize(
        serialization.serialize(SerializableFromSuperClassOne())),
    SerializableFromSuperClassOne())
self.assertEqual(
    serialization.deserialize(
        serialization.serialize(SerializableFromSuperClassTwo())),
    SerializableFromSuperClassTwo())
self.assertEqual(
    serialization.deserialize(
        serialization.serialize(SerializableFromSuperClassThree())),
    SerializableFromSuperClassThree())
