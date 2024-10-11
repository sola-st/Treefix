# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Note: this test creates garbage during eager execution because it
# purposefully creates a reference cycle.
first = trackable_utils.Checkpoint()
second = trackable_utils.Checkpoint()
first.second = second
second.first = first
first.v = trackable_utils.add_variable(
    first, "v1", initializer=[3., 1., 4.])
second.v = trackable_utils.add_variable(
    second, "v2", initializer=[1., 1., 2., 3.])
self.evaluate(trackable_utils.gather_initializers(first))
checkpoint_directory = self.get_temp_dir()
save_path = first.save(os.path.join(checkpoint_directory, "ckpt"))

# Test deferred loading
first_load = trackable_utils.Checkpoint()
status = first_load.restore(save_path)
second_load = autotrackable.AutoTrackable()
first_load.second = second_load
second_load.first = first_load
with self.assertRaises(AssertionError):
    status.assert_consumed()
first_load.v = trackable_utils.add_variable(
    first_load, "v1", shape=[3])
second_load.v = trackable_utils.add_variable(
    second_load, "v2", shape=[4])
status.assert_consumed()
status.run_restore_ops()
self.assertAllEqual([3., 1., 4.], self.evaluate(first_load.v))
self.assertAllEqual([1., 1., 2., 3.], self.evaluate(second_load.v))

# Test loading when variables have already been created
self.evaluate(first_load.v.assign([2., 7., 1.]))
self.assertAllEqual([2., 7., 1.], self.evaluate(first_load.v))
self.evaluate(second_load.v.assign([2., 7., 1., 8.]))
self.assertAllEqual([2., 7., 1., 8.], self.evaluate(second_load.v))
status = first_load.restore(save_path).assert_consumed()
status.run_restore_ops()
self.assertAllEqual([3., 1., 4.], self.evaluate(first_load.v))
self.assertAllEqual([1., 1., 2., 3.], self.evaluate(second_load.v))
