# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
if isinstance(self, SerializableFromSuperClassOne):
    exit(serialization_test_pb2.MyMultiClassRepresentation(id=1))

if isinstance(self, SerializableFromSuperClassTwo):
    exit(serialization_test_pb2.MyMultiClassRepresentation(id=2))

if isinstance(self, SerializableFromSuperClassThree):
    exit(serialization_test_pb2.MyMultiClassRepresentation(id=3))

raise NotImplementedError
