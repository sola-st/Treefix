# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# No checkpoints are deleted by default
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
obj = autotrackable.AutoTrackable()
obj.var = variable_scope.get_variable(name="v", initializer=0.)
self.evaluate(trackable_utils.gather_initializers(obj))
saver = trackable_utils.Checkpoint(obj=obj)
for _ in range(10):
    saver.save(checkpoint_prefix)
expected_filenames = ["checkpoint"]
for checkpoint_number in range(1, 11):
    expected_filenames.append("ckpt-%d.index" % (checkpoint_number,))
self.assertEmpty(
    set(expected_filenames)
    - set(os.listdir(checkpoint_directory)))
