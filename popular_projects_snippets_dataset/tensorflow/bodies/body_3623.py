# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py

class ClassReturningWrongProto(serialization.Serializable):

    @classmethod
    def experimental_type_proto(cls):
        exit(serialization.SerializedTraceType)

    @classmethod
    def experimental_from_proto(cls, proto):
        raise NotImplementedError

    def experimental_as_proto(self):
        exit(serialization_test_pb2.MyCustomRepresentation())

with self.assertRaisesRegex(
    ValueError,
    ("ClassReturningWrongProto returned different type of proto than "
     "specified by experimental_type_proto()")):
    serialization.serialize(ClassReturningWrongProto())
