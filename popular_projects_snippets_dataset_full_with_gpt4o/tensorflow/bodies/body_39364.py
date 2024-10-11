# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
directory = self.get_temp_dir()
mock_time.time.return_value = 10000.
checkpoint = util.Checkpoint()
first_manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=1, keep_checkpoint_every_n_hours=1.)
first_path = first_manager.save()
mock_time.time.return_value += 3600.
second_path = first_manager.save()
mock_time.time.return_value += 3600.
third_path = first_manager.save()
self.assertFalse(checkpoint_management.checkpoint_exists(first_path))
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
self.assertEqual([third_path], first_manager.checkpoints)
state = checkpoint_management.get_checkpoint_state(directory)
self.assertEqual(13600., state.last_preserved_timestamp)
# Set the clock back in time
mock_time.time.return_value = 5000.
del first_manager
with test.mock.patch.object(logging, "warning") as mock_log:
    second_manager = checkpoint_management.CheckpointManager(
        checkpoint, directory, max_to_keep=1)
    self.assertRegex(
        str(mock_log.call_args),
        "behind the last preserved checkpoint timestamp")
# We should err on the side of keeping checkpoints around when we're not
# sure whether they were preserved or not due to clock funkiness.
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
# We know about the existing checkpoints, but they'll never be deleted and
# so won't go in the CheckpointState proto on save.
self.assertEqual(third_path, second_manager.latest_checkpoint)
self.assertEqual([], second_manager.checkpoints)
mock_time.time.return_value += 10.
fourth_path = second_manager.save()
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
self.assertEqual(fourth_path, second_manager.latest_checkpoint)
self.assertEqual([fourth_path], second_manager.checkpoints)
mock_time.time.return_value += 10.
fifth_path = second_manager.save()
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
self.assertEqual([fifth_path], second_manager.checkpoints)
state = checkpoint_management.get_checkpoint_state(directory)
self.assertEqual(5000., state.last_preserved_timestamp)
self.assertEqual([5020.],
                 state.all_model_checkpoint_timestamps)
