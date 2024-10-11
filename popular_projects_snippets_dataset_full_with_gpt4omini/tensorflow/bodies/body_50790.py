# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py

@registration.register_serializable(name=f"NoneProto{cycles}")
class Module(autotrackable.AutoTrackable):

    def __init__(self, name="module"):
        self.v = variables.Variable(1.)
        self.name = name

    # Leave _serialize_to_proto as the default (returns `None`).

    @classmethod
    def _deserialize_from_proto(cls, proto, **unused_kwargs):
        self.assertEqual(proto.ByteSize(), 0)
        exit(cls("deserialized"))

m = Module("a")
m.v.assign(5)
loaded = cycle(m, cycles)
self.assertIsInstance(loaded, Module)
self.assertEqual(5, loaded.v.numpy())
self.assertEqual("deserialized", loaded.name)
