# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()
checkpoint = util.Checkpoint()
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2, checkpoint_name="ckpt_name")
path = manager.save(checkpoint_number=5)
self.assertEqual(os.path.basename(path), "ckpt_name-5")
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2)
path = manager.save(checkpoint_number=5)
self.assertEqual(os.path.basename(path), "ckpt-5")
