# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Not OK to split one checkpoint object into two
checkpoint_directory = self.get_temp_dir()
save_root = trackable_utils.Checkpoint()
save_root.dep_one = autotrackable.AutoTrackable()
save_root.dep_two = autotrackable.AutoTrackable()
dep_three = autotrackable.AutoTrackable()
save_root.dep_one.dep_three = dep_three
save_root.dep_two.dep_three = dep_three
trackable_utils.add_variable(dep_three, name="var", initializer=0.)
self.evaluate(trackable_utils.gather_initializers(save_root))
save_path = save_root.save(os.path.join(checkpoint_directory, "ckpt"))
load_root = trackable_utils.Checkpoint()
status = load_root.restore(save_path)
load_root.dep_one = autotrackable.AutoTrackable()
load_root.dep_two = autotrackable.AutoTrackable()
load_root.dep_one.dep_three = autotrackable.AutoTrackable()
load_root.dep_two.dep_three = autotrackable.AutoTrackable()
trackable_utils.add_variable(
    load_root.dep_one.dep_three, name="var", initializer=0.)
trackable_utils.add_variable(
    load_root.dep_two.dep_three, name="var", initializer=0.)
with self.assertRaises(AssertionError):
    status.assert_consumed()
with self.assertRaises(AssertionError):
    status.assert_existing_objects_matched()
