# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir() + "/no_checkpoints"
with self.assertRaises(errors_impl.OpError):
    self.assertAllEqual(
        checkpoint_utils.load_variable(checkpoint_dir, "var1"), [])
