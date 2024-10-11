# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
v = variables.Variable(1.0)
step_counter = variables.Variable(0)
self.evaluate([v.initializer, step_counter.initializer])
checkpoint = util.Checkpoint(v=v)
manager = checkpoint_management.CheckpointManager(
    checkpoint,
    self.get_temp_dir(),
    max_to_keep=None,
    step_counter=step_counter,
    checkpoint_interval=2)

# step_counter: 0, save an initial checkpoint.
path = manager.save(check_interval=True)
self.assertTrue(checkpoint_management.checkpoint_exists(path))

# step_counter: 1, no checkpoint saved.
self.evaluate(step_counter.assign_add(1))
path = manager.save(check_interval=True)
self.assertIsNone(path)

# step_counter: 2, checkpoint saved.
self.evaluate(step_counter.assign_add(1))
path = manager.save(check_interval=True)
self.assertTrue(checkpoint_management.checkpoint_exists(path))

# no checkpoint saved when calling `save` with the same step counter.
path = manager.save(check_interval=True)
self.assertIsNone(path)

# step_counter: 3, no checkpoint saved.
self.evaluate(step_counter.assign_add(1))
path = manager.save(check_interval=True)
self.assertIsNone(path)

# Always save the checkpoint.
path = manager.save(check_interval=False)
self.assertTrue(checkpoint_management.checkpoint_exists(path))
