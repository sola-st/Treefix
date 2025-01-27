# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
checkpoint = util.Checkpoint()
directory = os.path.join(
    self.get_temp_dir(),
    # Avoid sharing directories between eager and graph
    # TODO(allenl): stop run_in_graph_and_eager_modes reusing directories
    str(context.executing_eagerly()))
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=None)
first_path = manager.save()
second_path = manager.save()
third_path = manager.save()
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
self.assertTrue(checkpoint_management.checkpoint_exists(first_path))
self.assertEqual(third_path, manager.latest_checkpoint)
self.assertEqual([first_path, second_path, third_path],
                 manager.checkpoints)
del manager
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=None)
fourth_path = manager.save()
self.assertEqual([first_path, second_path, third_path, fourth_path],
                 manager.checkpoints)
del manager
manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=3)
self.assertEqual([first_path, second_path, third_path, fourth_path],
                 manager.checkpoints)
self.assertTrue(checkpoint_management.checkpoint_exists(fourth_path))
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
self.assertTrue(checkpoint_management.checkpoint_exists(first_path))
fifth_path = manager.save()
self.assertEqual([third_path, fourth_path, fifth_path],
                 manager.checkpoints)
self.assertTrue(checkpoint_management.checkpoint_exists(fifth_path))
self.assertTrue(checkpoint_management.checkpoint_exists(fourth_path))
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
self.assertFalse(checkpoint_management.checkpoint_exists(second_path))
self.assertFalse(checkpoint_management.checkpoint_exists(first_path))
