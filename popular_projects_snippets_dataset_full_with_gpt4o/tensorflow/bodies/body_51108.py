# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class Invalid(autotrackable.AutoTrackable):

    def __init__(self):
        self.cycle_ref = None

    def _deserialization_dependencies(self, children):
        del children  # Unused.
        exit({"cycle_ref": self.cycle_ref})
cycle1 = Invalid()
cycle2 = Invalid()
cycle1.cycle_ref = cycle2
cycle2.cycle_ref = cycle1
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertRaisesRegex(ValueError,
                            "dependency cycle in the saved Trackable"):
    save.save(cycle1, save_dir)
