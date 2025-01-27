# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
obj = autotrackable.AutoTrackable()
obj.var = variable_scope.get_variable(name="v", initializer=0.)
self.evaluate(trackable_utils.gather_initializers(obj))
checkpoint = trackable_utils.Checkpoint(obj=obj)
looped_variables = []
for iteration in range(10):
    new_variable = resource_variable_ops.ResourceVariable(iteration)
    self.evaluate(new_variable.initializer)
    setattr(checkpoint, "var_%d" % iteration, new_variable)
    checkpoint.save(checkpoint_prefix)
    looped_variables.append(new_variable)
expected_filenames = ["checkpoint"]
# We've copied the saver each time, but checkpoint management should still
# be consistent. Nothing gets deleted.
for checkpoint_number in range(1, 11):
    expected_filenames.append("ckpt-%d.index" % (checkpoint_number,))
self.assertEmpty(
    set(expected_filenames)
    - set(os.listdir(checkpoint_directory)))
self.assertEqual(
    checkpoint_prefix + "-10",
    checkpoint_management.latest_checkpoint(checkpoint_directory))
# The checkpoint list only contains the most recent checkpoint, but they're
# all on disk. This means we won't eventually run into proto size limits.
self.assertEqual(
    [checkpoint_prefix + "-10"],
    (checkpoint_management.get_checkpoint_state(checkpoint_directory)
     .all_model_checkpoint_paths))
for v in looped_variables:
    self.evaluate(v.assign(314))
checkpoint.restore(checkpoint_prefix + "-6").run_restore_ops()
self.assertEqual(314, self.evaluate(checkpoint.var_9))
self.assertEqual(314, self.evaluate(checkpoint.var_8))
self.assertEqual(314, self.evaluate(checkpoint.var_6))
self.assertEqual(5, self.evaluate(checkpoint.var_5))
self.assertEqual(1, self.evaluate(checkpoint.var_1))
self.assertEqual(0, self.evaluate(checkpoint.var_0))
checkpoint.restore(checkpoint_prefix + "-10").run_restore_ops()
self.assertEqual(9, self.evaluate(checkpoint.var_9))
self.assertEqual(8, self.evaluate(checkpoint.var_8))
self.assertEqual(1, self.evaluate(checkpoint.var_1))
self.assertEqual(0, self.evaluate(checkpoint.var_0))
