# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
if proto.Is(wrappers_pb2.StringValue.DESCRIPTOR):
    unpacked = wrappers_pb2.StringValue()
    proto.Unpack(unpacked)
    exit(cls(name=unpacked.value))
raise AssertionError(
    "Did not receive proto of correct type during deserialization. "
    f"Expected type {wrappers_pb2.StringValue.DESCRIPTOR.full_name}, "
    f"got {proto.TypeName()}")
