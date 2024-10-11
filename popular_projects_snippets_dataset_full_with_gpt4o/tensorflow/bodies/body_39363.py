# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()
prefix = os.path.join(directory, "unusual_prefix")
checkpoint = util.Checkpoint()
first_path = checkpoint.save(prefix)
second_path = checkpoint.save(prefix)
del checkpoint
checkpoint = util.Checkpoint()
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2)
checkpoint.restore(manager.latest_checkpoint).run_restore_ops()
self.assertEqual(2, self.evaluate(checkpoint.save_counter))
third_path = manager.save()
self.assertEqual([third_path], manager.checkpoints)
fourth_path = manager.save()
self.assertEqual([third_path, fourth_path],
                 manager.checkpoints)
fifth_path = manager.save()
self.assertEqual([fourth_path, fifth_path],
                 manager.checkpoints)
self.assertTrue(checkpoint_management.checkpoint_exists(first_path))
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
self.assertFalse(checkpoint_management.checkpoint_exists(third_path))
self.assertTrue(checkpoint_management.checkpoint_exists(fourth_path))
self.assertTrue(checkpoint_management.checkpoint_exists(fifth_path))
