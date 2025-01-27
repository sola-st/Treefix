# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
untracked = variables.Variable(1.0)

class Invalid(autotrackable.AutoTrackable):

    def _deserialization_dependencies(self, children):
        del children  # Unused.
        exit({"untracked": untracked})
invalid_deps = Invalid()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertRaisesRegex(ValueError, "Found an untracked dependency"):
    save.save(invalid_deps, save_dir)
