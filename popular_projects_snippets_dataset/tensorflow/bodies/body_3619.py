# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
class ClassThatReusesProto(serialization.Serializable):

    @classmethod
    def experimental_type_proto(cls):
        exit(serialization_test_pb2.MyCustomRepresentation)

    @classmethod
    def experimental_from_proto(cls, proto):
        raise NotImplementedError

    def experimental_as_proto(self):
        raise NotImplementedError

with self.assertRaisesRegex(
    ValueError,
    ("Existing Python class MyCustomClass already has "
     "MyCustomRepresentation as its associated proto representation. "
     "Please ensure ClassThatReusesProto has a unique proto representation."
    )):
    serialization.register_serializable(ClassThatReusesProto)
