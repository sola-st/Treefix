# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
save_root = trackable_utils.Checkpoint()
save_root.dep = autotrackable.AutoTrackable()
save_root.dep.var = trackable_utils.add_variable(
    save_root.dep, name="var", initializer=0.)
self.evaluate(state_ops.assign(save_root.dep.var, 12.))
first_path = save_root.save(os.path.join(checkpoint_directory, "first"))
self.evaluate(state_ops.assign(save_root.dep.var, 13.))
second_path = save_root.save(os.path.join(checkpoint_directory, "second"))

first_root = trackable_utils.Checkpoint()
second_root = trackable_utils.Checkpoint()
first_status = first_root.restore(first_path)
second_status = second_root.restore(second_path)
load_dep = autotrackable.AutoTrackable()
load_dep.var = trackable_utils.add_variable(
    load_dep, name="var", shape=[])
first_root.dep = load_dep
first_status.assert_consumed()
first_status.run_restore_ops()
self.assertEqual(12., self.evaluate(load_dep.var))
second_root.dep = load_dep
second_status.assert_consumed()
second_status.run_restore_ops()
self.assertEqual(13., self.evaluate(load_dep.var))

# Try again with the order of the restore() reversed. The last restore
# determines the final value.
first_root = trackable_utils.Checkpoint()
second_root = trackable_utils.Checkpoint()
second_status = second_root.restore(second_path)
first_status = first_root.restore(first_path)
load_dep = autotrackable.AutoTrackable()
load_dep.var = trackable_utils.add_variable(
    load_dep, name="var", shape=[])
first_root.dep = load_dep
first_status.assert_consumed()
first_status.run_restore_ops()
self.assertEqual(12., self.evaluate(load_dep.var))
second_root.dep = load_dep
second_status.assert_consumed()
second_status.run_restore_ops()
self.assertEqual(12., self.evaluate(load_dep.var))
