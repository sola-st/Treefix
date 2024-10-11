# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
saveable_state = SaveableState(5.)
trackable_state = TrackableState(10.)

# First test that SaveableState and TrackableState are equivalent by
# saving a checkpoint with both objects and swapping values.

self.assertEqual(5, self.evaluate(saveable_state.read()))
self.assertEqual(10, self.evaluate(trackable_state.read()))

ckpt_path = os.path.join(self.get_temp_dir(), "ckpt")
checkpoint.Checkpoint(a=saveable_state, b=trackable_state).write(ckpt_path)

status = checkpoint.Checkpoint(b=saveable_state,
                               a=trackable_state).read(ckpt_path)
status.assert_consumed()

self.assertEqual(10, self.evaluate(saveable_state.read()))
self.assertEqual(5, self.evaluate(trackable_state.read()))

# Test that the converted SaveableState is compatible with the checkpoint
# saved above.
to_convert = SaveableState(0.0)

converted_saveable_state = _create_converted_trackable(to_convert)

checkpoint.Checkpoint(a=converted_saveable_state).read(
    ckpt_path).assert_existing_objects_matched().expect_partial()
self.assertEqual(5, self.evaluate(to_convert.read()))

checkpoint.Checkpoint(b=converted_saveable_state).read(
    ckpt_path).assert_existing_objects_matched().expect_partial()
self.assertEqual(10, self.evaluate(to_convert.read()))
