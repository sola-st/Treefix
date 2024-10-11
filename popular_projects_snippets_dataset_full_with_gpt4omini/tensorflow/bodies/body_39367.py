# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()

# Create a checkpoint for initializing.
init_prefix = os.path.join(directory, "init")
init_v = variables.Variable(2.0)
init_ckpt = util.Checkpoint(v=init_v)
self.evaluate(init_v.initializer)
init_path = init_ckpt.save(init_prefix)

# Create the checkpoint manager.
ckpt_dir = os.path.join(directory, "ckpt")
v = variables.Variable(1.0)
checkpoint = util.Checkpoint(v=v)
manager = checkpoint_management.CheckpointManager(
    checkpoint,
    ckpt_dir,
    max_to_keep=None,
    init_fn=lambda: checkpoint.restore(init_path).run_restore_ops())
self.evaluate(v.initializer)

# First call should call `init_fn`.
self.assertIsNone(manager.restore_or_initialize())
self.assertEqual(2.0, self.evaluate(v))

# Save a checkpoint and second call should restore from the checkpoints.
manager.save()
self.assertIsNotNone(manager.restore_or_initialize())
