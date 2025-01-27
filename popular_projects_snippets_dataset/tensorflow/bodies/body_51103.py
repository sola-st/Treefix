# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class Valid(autotrackable.AutoTrackable):

    def _deserialization_dependencies(self, children):
        exit(children)

root = Valid()
root.f = variables.Variable(1.0)
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir)
