# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
with test_util.use_gpu():
    # Save an object-based checkpoint using a frozen saver
    directory = self.get_temp_dir()
    prefix = os.path.join(directory, "ckpt")
    v = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)
    checkpoint = trackable_utils.Checkpoint(v=v)
    self.evaluate(v.assign(3))
    # Create the save counter so assert_consumed doesn't complain about it not
    # existing in the checkpoint on restore.
    self.evaluate(checkpoint.save_counter.assign(12))
    saver = trackable_utils.frozen_saver(checkpoint)
    with ops.device("cpu:0"):
        prefix_tensor = constant_op.constant(prefix)
    self.evaluate(saver.save(prefix_tensor))
    self.evaluate(v.assign(10))
    # Use the frozen saver to restore the same object graph
    self.evaluate(saver.restore(prefix_tensor))
    self.assertEqual(3, self.evaluate(v))

    # Restore using another frozen saver on an identical object graph
    del v, checkpoint, saver
    v = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)
    checkpoint = trackable_utils.Checkpoint(v=v)
    saver = trackable_utils.frozen_saver(checkpoint)
    self.evaluate(saver.restore(prefix_tensor))
    self.assertEqual(3, self.evaluate(v))

    # Restore as an object-based checkpoint
    del v, checkpoint, saver
    checkpoint = trackable_utils.Checkpoint()
    status = checkpoint.restore(prefix)
    v = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)
    if context.executing_eagerly():
        self.assertEqual(12, self.evaluate(checkpoint.save_counter))
        self.assertEqual(0, self.evaluate(v))
    checkpoint.v = v
    status.assert_consumed().run_restore_ops()
    self.assertEqual(3, self.evaluate(v))
    self.assertEqual(12, self.evaluate(checkpoint.save_counter))
