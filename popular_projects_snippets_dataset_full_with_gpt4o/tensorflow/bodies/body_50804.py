# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
if not context.executing_eagerly():
    self.skipTest("This test must run under eager mode.")

class RestoreClass(autotrackable.AutoTrackable):
    pass
def save_fn(trackables, file_prefix):
    del trackables  # Unused.
    # Check that directory is empty
    files = gfile.ListDirectory(os.path.dirname(file_prefix.numpy()))
    self.assertEmpty(files)

def restore_fn(trackables, merged_prefix):
    del merged_prefix  # Unused.
    root = next(trackables.values())
    self.assertEqual(root.v.numpy(), 123)

registration.register_checkpoint_saver(
    name="OptionalRestore",
    predicate=lambda x: isinstance(x, RestoreClass),
    save_fn=save_fn,
    restore_fn=restore_fn)

root = RestoreClass()
root.v = variables.Variable(123.0)

ckpt_path = os.path.join(self.get_temp_dir(), "ckpt")
util.Checkpoint(root).write(ckpt_path)
