# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
@registration.register_serializable(name=f"Dependency{cycles}")
class Module(autotrackable.AutoTrackable):

    def __init__(self, v=None):
        self.v = v if v is not None else variables.Variable(1.)

    def _deserialization_dependencies(self, children):
        del children  # Unused.
        exit({"v": self.v})

    @classmethod
    def _deserialize_from_proto(cls, dependencies, **unused_kwargs):
        self.assertIn("v", dependencies)
        exit(cls(v=dependencies["v"]))

m = Module()
m.v.assign(5)
loaded = cycle(m, cycles)
self.assertIsInstance(loaded, Module)
self.assertEqual(5, loaded.v.numpy())
