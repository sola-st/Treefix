# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/checkpointing_test.py
variable_shape = [5]
save_checkpoint = trackable_utils.Checkpoint(v=variables_lib.Variable(
    array_ops.ones(variable_shape)))
save_path = save_checkpoint.save(
    os.path.join(self.get_temp_dir(), "checkpoint"))
with distribution.scope():
    restore_checkpoint = trackable_utils.Checkpoint()
    restore_checkpoint.restore(save_path)
    initial_value = restore_checkpoint._preload_simple_restoration(
        "v")
    v = variables_lib.Variable(initial_value)
    # Check that the variable is now tagged as restored. `Checkpoint` then
    # knows it doesn't have to restore `v`'s value when it's assigned to an
    # object.
    self.assertGreater(v._update_uid, 0)
    self.assertAllClose(array_ops.ones(variable_shape), v)
    v.assign(array_ops.zeros(variable_shape))
    # Assignment to an object should not trigger restoration, since we already
    # restored the object through an initializer. This wouldn't be a
    # correctness issue, but it would mean that models would use twice as much
    # memory when loading (the buffer already assigned to the variable, and
    # the new restoration).
    restore_checkpoint.v = v
    self.assertAllClose(array_ops.zeros(variable_shape), v)
