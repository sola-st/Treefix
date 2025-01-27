# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
my_custom = MyCustomClass(1234, "my_name")
serialized = serialization.serialize(my_custom)

self.assertTrue(
    serialized.representation.Is(
        serialization_test_pb2.MyCustomRepresentation.DESCRIPTOR))

proto = serialization_test_pb2.MyCustomRepresentation()
serialized.representation.Unpack(proto)
self.assertEqual(proto.index, my_custom.index)
self.assertEqual(proto.name, my_custom.name)
