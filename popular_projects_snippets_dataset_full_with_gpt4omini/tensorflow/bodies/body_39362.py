# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()
mock_time.time.return_value = 3.
checkpoint = util.Checkpoint()
first_manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=2)
first_time = 10000.
first_name = os.path.join(directory, "ckpt-1")
mock_time.time.return_value = first_time
first_manager.save()
state = checkpoint_management.get_checkpoint_state(directory)
second_time = first_time + 3610.
second_name = os.path.join(directory, "ckpt-2")
mock_time.time.return_value = second_time
first_manager.save()
state = checkpoint_management.get_checkpoint_state(directory)
self.assertEqual([first_time, second_time],
                 state.all_model_checkpoint_timestamps)
self.assertEqual([first_name, second_name], first_manager.checkpoints)
self.assertEqual(second_name, first_manager.latest_checkpoint)
del first_manager

second_manager = checkpoint_management.CheckpointManager(
    checkpoint, directory,
    max_to_keep=2, keep_checkpoint_every_n_hours=1.5)
self.assertEqual([first_name, second_name], second_manager.checkpoints)
self.assertEqual(second_name, second_manager.latest_checkpoint)
third_name = os.path.join(directory, "ckpt-3")
third_time = second_time + 3600. * 0.2
mock_time.time.return_value = third_time
second_manager.save()
self.assertTrue(checkpoint_management.checkpoint_exists(first_name))
self.assertTrue(checkpoint_management.checkpoint_exists(second_name))
self.assertEqual([second_name, third_name],
                 second_manager.checkpoints)
state = checkpoint_management.get_checkpoint_state(directory)
self.assertEqual(first_time, state.last_preserved_timestamp)
fourth_time = third_time + 3600. * 0.5
mock_time.time.return_value = fourth_time
fourth_name = os.path.join(directory, "ckpt-4")
second_manager.save()
self.assertTrue(checkpoint_management.checkpoint_exists(first_name))
self.assertFalse(checkpoint_management.checkpoint_exists(second_name))
self.assertEqual([third_name, fourth_name],
                 second_manager.checkpoints)
fifth_time = fourth_time + 3600. * 0.5
mock_time.time.return_value = fifth_time
fifth_name = os.path.join(directory, "ckpt-5")
second_manager.save()
self.assertEqual([fourth_name, fifth_name],
                 second_manager.checkpoints)
state = checkpoint_management.get_checkpoint_state(directory)
self.assertEqual(first_time, state.last_preserved_timestamp)
del second_manager
third_manager = checkpoint_management.CheckpointManager(
    checkpoint, directory,
    max_to_keep=2, keep_checkpoint_every_n_hours=1.5)
self.assertEqual(fifth_name, third_manager.latest_checkpoint)
mock_time.time.return_value += 10.
third_manager.save()
sixth_name = os.path.join(directory, "ckpt-6")
state = checkpoint_management.get_checkpoint_state(directory)
self.assertEqual(fourth_time, state.last_preserved_timestamp)
self.assertTrue(checkpoint_management.checkpoint_exists(first_name))
self.assertTrue(checkpoint_management.checkpoint_exists(fourth_name))
self.assertTrue(checkpoint_management.checkpoint_exists(fifth_name))
self.assertTrue(checkpoint_management.checkpoint_exists(sixth_name))
self.assertFalse(checkpoint_management.checkpoint_exists(second_name))
self.assertFalse(checkpoint_management.checkpoint_exists(third_name))
self.assertEqual([fifth_name, sixth_name],
                 third_manager.checkpoints)
