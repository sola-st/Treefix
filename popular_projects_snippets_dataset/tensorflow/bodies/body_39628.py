# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Currently fine to load two checkpoint objects into one Python object
checkpoint_directory = self.get_temp_dir()
save_root = trackable_utils.Checkpoint()
save_root.dep_one = autotrackable.AutoTrackable()
save_root.dep_two = autotrackable.AutoTrackable()
trackable_utils.add_variable(
    save_root.dep_one, name="var1", initializer=32., dtype=dtypes.float64)
trackable_utils.add_variable(
    save_root.dep_two, name="var2", initializer=64., dtype=dtypes.float64)
self.evaluate(trackable_utils.gather_initializers(save_root))
save_path = save_root.save(os.path.join(checkpoint_directory, "ckpt"))
load_root = trackable_utils.Checkpoint()
load_root.dep_one = autotrackable.AutoTrackable()
load_root.dep_two = load_root.dep_one
v1 = trackable_utils.add_variable(
    load_root.dep_one, name="var1", shape=[], dtype=dtypes.float64)
v2 = trackable_utils.add_variable(
    load_root.dep_one, name="var2", shape=[], dtype=dtypes.float64)
status = load_root.restore(
    save_path).assert_consumed().assert_existing_objects_matched()
status.run_restore_ops()
self.assertEqual(32., self.evaluate(v1))
self.assertEqual(64., self.evaluate(v2))
