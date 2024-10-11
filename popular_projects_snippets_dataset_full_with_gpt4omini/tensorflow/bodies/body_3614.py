# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
my_composite = MyCompositeClass(
    MyCustomClass(1, "name_1"), MyCustomClass(2, "name_2"),
    MyCustomClass(3, "name_3"))
serialized = serialization.serialize(my_composite)

self.assertTrue(
    serialized.representation.Is(
        serialization_test_pb2.MyCompositeRepresentation.DESCRIPTOR))

proto = serialization_test_pb2.MyCompositeRepresentation()
serialized.representation.Unpack(proto)

self.assertEqual(proto.elements[0],
                 serialization.serialize(MyCustomClass(1, "name_1")))
self.assertEqual(proto.elements[1],
                 serialization.serialize(MyCustomClass(2, "name_2")))
self.assertEqual(proto.elements[2],
                 serialization.serialize(MyCustomClass(3, "name_3")))
