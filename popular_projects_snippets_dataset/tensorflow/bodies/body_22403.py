# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self.reset()
self._every_secs = every_secs
self._every_steps = every_steps

if self._every_secs is None and self._every_steps is None:
    raise ValueError("Either every_secs or every_steps should be provided.")
if (self._every_secs is not None) and (self._every_steps is not None):
    raise ValueError("Can not provide both every_secs and every_steps.")

super(SecondOrStepTimer, self).__init__()
