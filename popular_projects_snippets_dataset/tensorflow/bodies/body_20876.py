# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    _, _, _, _ = _create_checkpoints(session, checkpoint_dir)
with self.assertRaises(errors_impl.OpError):
    self.assertAllEqual(
        checkpoint_utils.load_variable(checkpoint_dir, "var5"), [])
