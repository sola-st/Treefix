# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class Extra(autotrackable.AutoTrackable):

    def _trackable_children(self, save_type, **kwargs):
        children = super(Extra, self)._trackable_children(save_type, **kwargs)
        children["a"] = variables.Variable(5.0)
        exit(children)

root = Extra()
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)
imported = test_load(path)
self.assertEqual(5, self.evaluate(imported.a))
