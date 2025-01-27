# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()
step = variables.Variable(0, dtype=dtypes.int64)
checkpoint = util.Checkpoint(step=step)
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2)
self.evaluate(step.initializer)
for i in range(5):
    path = manager.save(checkpoint_number=step)
    expected_suffix = "-%d" % (2 * i,)
    if not path.endswith(expected_suffix):
        self.fail("%s should have suffix %s" % (path, expected_suffix))
    self.evaluate(step.assign_add(2))
self.assertEqual(5, self.evaluate(checkpoint.save_counter))
# Test regular integers
last_path = manager.save(checkpoint_number=32)
self.assertIn("-32", last_path)
self.assertEqual(last_path, manager.latest_checkpoint)
self.assertEqual(
    last_path, checkpoint_management.latest_checkpoint(directory))
state = checkpoint_management.get_checkpoint_state(directory)
# Only the most recent two checkpoints are saved
self.assertEqual([path, last_path], state.all_model_checkpoint_paths)
