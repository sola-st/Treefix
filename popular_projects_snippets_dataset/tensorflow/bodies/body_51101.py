# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
# Test that `tf.saved_model.save` API returns None to user.
root = autotrackable.AutoTrackable()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
result = save.save(root, save_dir)
self.assertIsNone(result)
