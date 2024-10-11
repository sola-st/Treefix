# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.assertRaises(ValueError):
    basic_session_run_hooks.StopAtStepHook(num_steps=10, last_step=20)
