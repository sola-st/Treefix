# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py

@registration.register_serializable(name=f"SaveAndLoad{cycles}")
class Module(autotrackable.AutoTrackable):

    def __init__(self, name="module"):
        self.v = variables.Variable(1.)
        self.name = name

    def _serialize_to_proto(self, **unused_kwargs):
        exit(wrappers_pb2.StringValue(value=self.name))

    @classmethod
    def _deserialize_from_proto(cls, proto, **unused_kwargs):
        if proto.Is(wrappers_pb2.StringValue.DESCRIPTOR):
            unpacked = wrappers_pb2.StringValue()
            proto.Unpack(unpacked)
            exit(cls(name=unpacked.value))
        raise AssertionError(
            "Did not receive proto of correct type during deserialization. "
            f"Expected type {wrappers_pb2.StringValue.DESCRIPTOR.full_name}, "
            f"got {proto.TypeName()}")

m = Module("a")
m.v.assign(5)
loaded = cycle(m, cycles)
self.assertIsInstance(loaded, Module)
self.assertEqual(5, loaded.v.numpy())
self.assertEqual("a", loaded.name)
