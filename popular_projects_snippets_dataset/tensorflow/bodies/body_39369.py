# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = pathlib.Path(self.get_temp_dir())
checkpoint = util.Checkpoint()
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2, checkpoint_name="ckpt_name")
manager.save()

cp_dir = checkpoint_management.latest_checkpoint(directory)
self.assertEqual(str(directory / "ckpt_name-1"), cp_dir)
