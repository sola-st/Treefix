# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.assertRaises(ValueError):
    basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir, saver=self.scaffold.saver, scaffold=self.scaffold)
