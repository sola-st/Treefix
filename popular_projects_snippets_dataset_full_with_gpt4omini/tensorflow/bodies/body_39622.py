# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py

class Dependency(autotrackable.AutoTrackable):

    def build(self):
        self.var = trackable_utils.add_variable(
            self, "var", initializer=0.)

class LateDependencies(trackable_utils.Checkpoint):

    def add_dep(self):
        self.dep = Dependency()
        self.dep.build()

original = LateDependencies()
original.add_dep()
self.evaluate(state_ops.assign(original.dep.var, 123.))
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = original.save(checkpoint_prefix)
load_into = LateDependencies()
status = load_into.restore(save_path)
status.assert_existing_objects_matched()
with self.assertRaises(AssertionError):
    status.assert_consumed()
load_into.add_dep()
status.assert_consumed()
status.assert_existing_objects_matched().run_restore_ops()
self.assertEqual(123., self.evaluate(load_into.dep.var))
