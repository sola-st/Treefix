# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()
v = variables.Variable(1.0)
step_counter = variables.Variable(0)
self.evaluate([v.initializer, step_counter.initializer])

# Prepare a checkpoint.
checkpoint = util.Checkpoint(v=v)
checkpoint.save(os.path.join(directory, "ckpt"))

manager = checkpoint_management.CheckpointManager(
    checkpoint,
    directory,
    max_to_keep=None,
    step_counter=step_counter,
    checkpoint_interval=2)

# Restore from the checkpoint.
self.assertIsNotNone(manager.restore_or_initialize())

# step_counter: 0, no checkpoint saved because it is restored from the
# checkpoint with the same step.
path = manager.save()
self.assertIsNone(path)
