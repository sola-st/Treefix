# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
model = self._create_trackable()
model.v.assign(3.)
separate_variable = variables_lib.Variable(5.)

with self.assertRaisesRegex(ValueError, "root.v already exists"):
    trackable_utils.Checkpoint(model, v=separate_variable)

checkpoint = trackable_utils.Checkpoint(
    model, separate_variable=separate_variable)
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = checkpoint.save(checkpoint_prefix)

# Case 1: Loading checkpoint with same configuration.
new_model = self._create_trackable()
separate_variable = variables_lib.Variable(1.)
load_checkpoint = trackable_utils.Checkpoint(
    new_model, separate_variable=separate_variable)
load_checkpoint.restore(save_path).assert_consumed()
self.assertEqual(self.evaluate(new_model.v), 3)
self.assertEqual(self.evaluate(separate_variable), 5)
self.assertEqual(self.evaluate(load_checkpoint.save_counter), 1)

# Case 2: Loading checkpoint where v and separate_variable are swapped:
# v is not attached to the root, while separate variable is attached to root
new_model = autotrackable.AutoTrackable()
new_model.separate_variable = variables_lib.Variable(200.)
v = variables_lib.Variable(100.)
load_checkpoint = trackable_utils.Checkpoint(new_model, v=v)
load_checkpoint.restore(save_path).assert_consumed()
self.assertEqual(self.evaluate(v), 3)
self.assertEqual(self.evaluate(new_model.separate_variable), 5)
self.assertEqual(self.evaluate(load_checkpoint.save_counter), 1)

# Case 3: Loading checkpoint where no root object is specified
separate_variable = variables_lib.Variable(200.)
v = variables_lib.Variable(100.)
load_checkpoint = trackable_utils.Checkpoint(
    v=v, separate_variable=separate_variable)
load_checkpoint.restore(save_path).assert_consumed()
self.assertEqual(self.evaluate(v), 3)
self.assertEqual(self.evaluate(new_model.separate_variable), 5)
self.assertEqual(self.evaluate(load_checkpoint.save_counter), 1)
