# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py

if (every_n_steps is None) == (every_n_secs is None):
    raise ValueError(
        "exactly one of every_n_steps and every_n_secs should be provided.")
self._timer = SecondOrStepTimer(
    every_steps=every_n_steps, every_secs=every_n_secs)

self._summary_writer = summary_writer
self._output_dir = output_dir
self._last_global_step = None
self._steps_per_run = 1
