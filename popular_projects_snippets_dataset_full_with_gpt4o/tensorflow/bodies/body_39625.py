# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py

class Dependency(autotrackable.AutoTrackable):

    def build(self):
        self.var = trackable_utils.add_variable(
            self, "var", initializer=0.)

class DepAfterVar(trackable_utils.Checkpoint):

    def add_dep(self):
        dep = Dependency()
        dep.build()
        self.dep = dep

dep_after_var = DepAfterVar()
dep_after_var.add_dep()
self.evaluate(state_ops.assign(dep_after_var.dep.var, -14.))
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = dep_after_var.save(checkpoint_prefix)

loaded_dep_after_var = DepAfterVar()
status = loaded_dep_after_var.restore(save_path)
loaded_dep_after_var.add_dep()
status.assert_consumed()
status.run_restore_ops()
self.assertEqual(-14., self.evaluate(loaded_dep_after_var.dep.var))
