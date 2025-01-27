# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = pathlib.Path(self.get_temp_dir())
v = variables.Variable(0.0)
checkpoint = util.Checkpoint(v=v)
self.evaluate(v.initializer)
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2, checkpoint_name="ckpt_name")
save_path = manager.save()
expected = str(directory / "ckpt_name-1")
self.assertEqual(expected, save_path)

restore_path = manager.restore_or_initialize()
self.assertEqual(str(directory / "ckpt_name-1"), restore_path)
